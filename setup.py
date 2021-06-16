from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="DataSUS",
    version="1.0",
    description="DataSUS analysis",
    packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=required,
)