from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .' # creating a constant # the -e . maps the setup.py to the requirements file

def get_requirements(file_path:str)->List[str]: # returns a list of string
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj: # open the file
        requirements=file_obj.readlines() # read the file line by line
        requirements=[req.replace("\n","") for req in requirements] # remove the new line character

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # remove the '-e .' from the list

    return requirements 

setup(
    name = 'mlproject',
    version='0.0.1',
    author='Chandan',
    author_email='chandanmalakar6209@gmail.com',
    packages=find_packages(), #find the directories which contains __init__.py file
    install_requires=get_requirements('requirements.txt') # list of requirements
)