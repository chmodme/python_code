#!/usr/bin/env python3
# Author: shaoyan

"""
比较两个数大小
"""

def f1(x, y):
    c = x
    d = y
    if c > d:
        return c
    else:
        return d

a = 10
b = 20

result = f1(a, b)

print(result)

print(dir())