from setuptools import find_packages,setup

from typing import List

HYPE_E = '-e .'

def get_requirements(file_path:str)->List[str]:

      '''
      This function returns list of requirements

      '''
      requirements = []

      with open(file_path)  as file_obj:
          requirements=file_obj.readlines()
          requirements=[req.replace("\n"," ").strip() for req in requirements]
          if HYPE_E in requirements:
               requirements.remove(HYPE_E)
          
      return requirements


setup(
  
  name="ML_Project",
  version="0.0.1",
  author = "SaiSriRam",
  author_email = "saisriram101201@gmail.com",
  packages = find_packages(),
  install_requires = get_requirements('requirements.txt')
)