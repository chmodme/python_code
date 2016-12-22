#!/usr/bin/env python3
# Author: shaoyan

"""
模拟用户登录：

"""
import json,sys

data ={}

# 定义添加用户函数
def add_user():
    # 读取文件原有数据：
    with open("user2.json", 'r') as j:
        user = json.load(j)
    # 接收用户输入
    username = str(input("输入用户名："))
    password = str(input("输入密码："))
    # 追加到字典
    user[username] = password
    if user[username] != 0:
        print("添加完成")
    # 将字典写入文件
    with open("user2.json", 'w') as f:
        json.dump(user,f)

def login():
    with open("user2.json", 'r') as j:
        user = json.load(j)
    for i in range(4):
        if i < 3:
            username = input("请输入你的用户名：")
            password = input("请输入你的密码：")
            if username in user.keys():  # 判断用户名是否在字典里
                if user[username] == str(password):  # 判断密码是否正确
                    print("登录成功！")
                    break
                else:
                    print("用户名或者密码错误，请重新输入！")
            else:
                print("用户名或者密码错误，请重新输入！")
        else:
            print("尝试次数超过3次，用户被锁定！请2个小时后再尝试")
            break

temp = input("输入 a 注册用户，回车继续：")
if temp == "a":
    add_user()

print("输入你的用户名和密码信息，进行登录")
login()