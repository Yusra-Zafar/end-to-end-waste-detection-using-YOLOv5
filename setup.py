from setuptools import find_packages, setup

setup(
    name = 'wasteDetection',
    version= '0.0.0',
    author= 'Yusra Zafar',
    author_email= 'yuxraz@gmail.com',
    description= 'End-to-end Waste Detection using YOLOv5',
    packages= find_packages(),  # to import all the packages in the project locally. it will look for the constructor file and will make that folder as a package.
    install_requires = []

)