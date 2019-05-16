#!/usr/bin/env python3
"""
setup.py
Boucher, Govedič, Saowakon, Swanson 2019

Setup script for installation.

"""
import setuptools


with open('README.md') as f:
    long_description = f.read()


setuptools.setup(
    name="shuffle-sum",
    version="0.0.1",
    author="Boucher, Govedič, Saowakon, Swanson",
    description="Tallying of single transferable vote ballots using the Shuffle-Sum protocol.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cryptovoting/shuffle-sum",
    packages=setuptools.find_packages(),
    install_requires=[
        'damgard-jurik',
        'gmpy2',
        'tqdm'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
