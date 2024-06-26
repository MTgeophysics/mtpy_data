#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

setup_requirements = []

test_requirements = ["pytest>=3"]

setup(
    author="Jared Peacock",
    author_email="jpeacock@usgs.gov",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="Test Data for MTpy",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="mtpy_data",
    name="mtpy_data",
    packages=find_packages(include=["mtpy_data", "mtpy_data.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/MTgeophysics/mtpy_data",
    version="0.0.1",
    zip_safe=False,
    package_data={
        "": [
            "mtpy_data/data/profile/*.edi",
            "mtpy_data/data/grid/*.edi",
            "mtpy_data/forward_models/Faults/*.edi",
            "mtpy_data/forward_models/HalfSpace/*.edi",
            "mtpy_data/forward_models/HalfSpaceSQC/*.edi",
            "mtpy_data/forward_models/HalfSpaceSQR/*.edi",
            "mtpy_data/forward_models/LayeredHalfSpace/*.edi",
            "mtpy_data/forward_models/NearSquareConductor/*.edi",
            "mtpy_data/forward_models/NEConductor/*.edi",
            "mtpy_data/forward_models/NEFaults/*.edi",
        ]
    },
)
