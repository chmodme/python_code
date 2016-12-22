#!/usr/bin/env python3
# Author: shaoyan

"""
if 语句
"""

user = "shaoyan"
passwd = "123456"

username = input("please input username:")
password = input("please input password:")

if user == username and passwd == password:
    print("欢迎登陆！")
else:
    print("invalid username or  password")