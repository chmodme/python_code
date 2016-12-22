#!/usr/bin/env python3
# Author: shaoyan

"""
格式化字符串
"""
# 每行最多不超过 80 个字符

name = 'shaoyan'
age = 22
job = 'sa'

msg = '''
information of user %s:
-------------------
name:   %s
age:    %d
job:    %s
--------End--------
''' %(name, name, age, job)

print(msg)