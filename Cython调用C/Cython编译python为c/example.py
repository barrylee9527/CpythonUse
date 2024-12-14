#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@Author: barrylee9527
@Filename: example.py
@Createdtime: 2024/12/14 16:48
@Description: 
"""
import time

import test
time1 = time.time()
test.calculate_pi(10000000)
time2 = time.time()
print("time cost:", time2 - time1)
if __name__ == '__main__':
    pass
