from setuptools import setup, find_packages

setup(
    name="pyvenv",
    version="0.1.0",
    author="Lucas Maciel",
    author_email="macieldfaria@gmail.com",
    description="A tool to manage virtual environments with PyEnv",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AjudanteMaciel/pyvenv",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
