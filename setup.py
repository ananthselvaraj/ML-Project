from setuptools import find_packages,setup
from typing import List


Hyben='-e.'
def get_requirments(file_path:str)->List[str]:

    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace('\n','') for req in requirments]


        if Hyben in requirments:
            requirments.remove(Hyben)
    return requirments
    

setup(
name='mlproject',
version='0.0.1',
author='Ananth',
author_email='ananthsa20@gmial.com',
packages=find_packages(),
install_requires=get_requirments('requirments.txt')
)