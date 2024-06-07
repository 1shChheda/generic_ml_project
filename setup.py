from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # this will read each line of the file, but also read '\n' at the end. We need to remove that
        [req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='generic_ml_project',
    version='0.0.1',
    author='Vansh Chheda',
    author_email='vansh.h.chheda@gmail.com',
    packages=find_packages(),
    # install_requires=['numpy','pandas','scikit-learn','matplotlib','seaborn','jupyter'], # in practical project, many more libraries might be required. 

    # Thus we create a fn. to get these libraries from 'requirements.txt'

    install_requires=get_requirements('requirements.txt'),
)