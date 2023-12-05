from setuptools import find_packages, setup
from src.data import make_dataset
setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='find association rule',
    author='peerapong',
    license='MIT',
)
