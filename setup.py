from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT= '-e .'

def get_requirements(file_path:str)-> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        

        return requirements



setup(
    name='DiamondPricePrediction',
    version='0.1.0',
    author='Arko Kundu',
    author_email="arkokundu500@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)