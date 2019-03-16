from setuptools import setup

with open("README.md", "r") as README_file:
    long_description = README_file.read()

setup(
    name='minesweeperPy',
    version='1.1',
    description='A Python 3 minesweeper generator module',
    license="MIT",
    long_description=long_description,
    author='stshrewsburyDev',
    author_email='',
    url="https://github.com/stshrewsburyDev/minesweeperPy",
    packages=["minesweeperPy"],
    install_requires=[]
)
