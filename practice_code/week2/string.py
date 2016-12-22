#!/usr/bin/env python3
# Author: shaoyan

"""
字符串处理
"""

names = "yan,jack,rain"
name2 = names.split(",")
# print(name2)
# print("|".join(name2))

# username =input("input your username:")
#if username.strip() == 'yan':   # strip 除去字符串两边的空格
#    print("welcome")

name = "yan"
print(name.center(20, '='))
print(name.find("y"))  # 查找，匹配第一个
