from setuptools import find_packages, setup 
from typing import List 

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:

    '''
    this function will return the list of packages from requirements.txt'''
    
    packages = []
    with open(file_path) as file_obj:
        packages = file_obj.readlines()
        packages = [req.replace("\n", "") for req in packages]

        if HYPEN_E_DOT in packages:
            packages.remove(HYPEN_E_DOT)

    return packages



setup(

    name = 'mlproject' ,  
    version = '0.0.1' , 
    author = 'Julian' , 
    author_email = 'lf2primelf2@gmial.com' , 
    packages = find_packages() , 
    install_requires = get_requirements('requirements.txt') 

)