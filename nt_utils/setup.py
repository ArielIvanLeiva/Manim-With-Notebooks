from setuptools import setup, find_packages

setup(
    name="nt_utils",
    version="0.1.0",
    packages=find_packages(include=["nt_utils"]),
    description="A simple library for customized jupyter notebooks exports",
    author="Ariel Leiva",
    install_requires=["nbformat"]
)
