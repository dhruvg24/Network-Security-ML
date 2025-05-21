'''
Essential for packaging and distribution of Py project. It helps to define the configuration of the project such as metadata, dependencies etc.
'''

from setuptools import find_packages,setup
from typing import List
# will search for __init__.py file

def get_requirements()->List[str]:
    '''Will return list of requirements from txt file'''
    requirement_list:List[str]=[];
    try:
        with open('requirements.txt') as file:
            lines = file.readlines();
            # process each lines
            for line in lines:
                requirement = line.strip()
                # ignore empty lines, -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print('requirement.txt file not found.')

    return requirement_list; 

# print(get_requirements())

setup(
    name='NetworkSecurityML',
    version='0.0.1',
    author='Dhruv Garg',
    author_email='dhruv02.work@gmail.com',
    packages =find_packages(),
    install_requires =get_requirements()
)