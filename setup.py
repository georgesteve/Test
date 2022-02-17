from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Test",
    version="0.1.0",
    author="George Steve",
    author_email="george.fajardo.s@uni.pe",
    description="Esta es una librería para aprendizaje de construcción de clases y su importación.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/georgesteve/Test/",
    license="Apache",
    packages=find_packages()
)
