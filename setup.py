from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        lines = file_obj.readlines()
        for line in lines:
            # Remove newline characters
            line = line.strip()

            # Check if the line contains the editable install flag '-e .'
            if line == HYPEN_E_DOT:
                continue

            # Split the line into package name and version
            package_info = line.split('==')

            # Add package name and version to requirements
            if len(package_info) == 2:
                requirements.append(f"{package_info[0]}=={package_info[1]}")

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='wajahat',
    author_email='wajahatalibasharat073@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
