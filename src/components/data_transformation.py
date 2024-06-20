import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj
from dataclasses import dataclass

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer # NEW: to fill in missing values within the dataset (with "mean", "median", "most_frequent", etc)
from sklearn.pipeline import Pipeline

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl') # to create a pickle file for preprocessor

class DataTransformation:

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_transformer_obj(self):
        # basically gonna be used to create all the pickle files used for feature engg., scaling, etc

        try:
            numerical_features = ['reading score', 'writing score']
            categorical_features = [
                'gender', 
                'race/ethnicity', 
                'parental level of education', 
                'lunch',
                'test preparation course'
            ]

            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"numerical features: {numerical_features}")
            logging.info(f"categorical features: {categorical_features}")

            # now, COMBINE & execute the numerical & categorical pipeline using "ColumnTransformer"
            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_features),
                    ("categorical_pipeline", categorical_pipeline, categorical_features)
                ]
            )

            logging.info("column transformer ready")

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("read train test data completed")
            
            logging.info("obtaining preprocessing object")
            # previously, we just created a template for the preprocessor
            # now, we'll use that to actually create a preprocessor object (over the train/test data) & STORE IT IN A PICKLE FILE
            preprocessor_obj = self.get_transformer_obj()

            target_column_name = "math score"

            # getting the training/testing data
            input_features_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_features_train_df = train_df[target_column_name]

            input_features_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_features_test_df = test_df[target_column_name]


            input_features_train_arr = preprocessor_obj.fit_transform(input_features_train_df)
            input_features_test_arr = preprocessor_obj.transform(input_features_test_df)
            logging.info("applied preprocessing object on train/test dataframe")

            # now, we combine these transformed input features with target features (to complete the "processed datasets")

            # we concatenate input/target arrays "along the second axis (columns)" using "np.c_"

            train_arr = np.c_[
                input_features_train_arr,
                np.array(target_features_train_df)
            ]

            test_arr = np.c_[
                input_features_test_arr,
                np.array(target_features_test_df)
            ]

            save_obj(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )
            logging.info("saved preprocessor object in pickle file")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)