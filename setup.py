#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-clover",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap-clover"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests", 'genson', 'pandas'
    ],
    entry_points="""
    [console_scripts]
    tap-clover=tap-clover:main
    """,
    packages=["tap-clover"],
    package_data = {
        "schemas": ["tap-clover/schemas/*.json"]
    },
    include_package_data=True,
)
