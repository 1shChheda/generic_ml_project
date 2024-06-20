# to use CustomExceptions
import os
import sys
from src.exception import CustomException
from src.logger import logging

from src.components.data_transformation import DataTransformation, DataTransformationConfig

# for working with data
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # NEW STUFF: to create class variables

@dataclass
    # "@dataclass" is a decorator, which will allow us to define Class variables directly (without the use of "__init__" function inside the Class)
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv') # the "trained data" will be stored at "artifacts" folder
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # so the above 3 paths will be saved here

    def initiate_data_ingestion(self):
        # to read the dataset
        logging.info("initialized data ingestion")
        try:
            df = pd.read_csv('notebook/data/StudentsPerformance.csv')
            logging.info("data ingestion: reading dataset")

            # to create the training_data folder/file
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("train test split initialized")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("data ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                # this information will be required for "data transformation"
            )

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data, test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)