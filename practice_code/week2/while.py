#!/usr/bin/env python3
# Author: shaoyan

"""
while 语句
"""
count =0

while True:
    count += 1
    if count > 50 and count < 60:   # 跳过 50~60
        continue
    print(count)

    if count == 100:
        break
