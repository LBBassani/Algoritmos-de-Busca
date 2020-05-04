
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='busca-lbbassani',  
     version='0.1',
     author="Lorena B Bassani",
     author_email="lorenabassani12@gmail.com",
     description="Algoritmos de Busca",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/LBBassani/Algoritmos-de-Busca",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
         "Operating System :: OS Independent",
         "Development Status :: 2 - Pre-Alpha",
     ],
     python_requires='>=3.7',
 )