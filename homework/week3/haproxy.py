#!/usr/bin/env python3
# Author: shaoyan
import json

"""
需求：
1. 根据用户输入，输出对应的backend下的server信息
2. 可添加backend 和sever信息
3. 可修改backend 和sever信息
4. 可删除backend 和sever信息
5. 操作配置文件前进行备份
6. 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；
    若信息与已有信息重复则不操作
"""

# 读取 backend 的 server 信息
def fetch_info(backend):
    info = []
    with open('ha.conf', 'r', encoding="utf-8") as f:
        for line in f:
            info.append(line)
    return info

print(fetch_info("www.xsy.me"))