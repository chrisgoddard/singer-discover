#!/usr/bin/env python

from setuptools import setup

setup(
    name="singer-discover-catalog",
    version="0.1.0",
    description="Edit a catalog from a tap's discovery mode",
    author="Chris Goddard",
    url="https://github.com/chrisgoddard",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["singer_discover"],
    install_requires=[
        "singer-python>=5.4.1,<6.0",
        "PyInquirer==1.0.3"
    ],
    entry_points="""
    [console_scripts]
    singer-discover=singer_discover:main
    """,
    packages=["singer_discover"],
    include_package_data=True,
)
