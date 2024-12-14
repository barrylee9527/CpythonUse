#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@Author: barrylee9527
@Filename: test_square.py.py
@Createdtime: 2024/12/14 16:45
@Description: 
"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["test.py"])
)

if __name__ == '__main__':
    pass
