#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@Author: barrylee9527
@Filename: test_square.py.py
@Createdtime: 2024/12/14 16:35
@Description: 
"""
from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("example", sources=["example.pyx", "example.c"]),
]

setup(
    ext_modules=cythonize(extensions),
)

