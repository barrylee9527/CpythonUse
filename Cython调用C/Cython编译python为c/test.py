#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@Author: barrylee9527
@Filename: test.py
@Createdtime: 2024/12/14 16:45
@Description: 
"""
def calculate_pi(count: int) -> float:
    result = 0.0
    positive = True
    for i in range(count):
        tmp = 1.0 / float(i * 2 + 1)
        if positive:
            result += tmp
        else:
            result -= tmp
        positive = not positive
    return result * 4.0
if __name__ == '__main__':
    pass
