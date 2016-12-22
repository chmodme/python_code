#!/usr/bin/env python3
# Author: shaoyan

"""
练习代码
"""

# 取数据：将域名对应的配置取到列表
def fetch(backend):
    result = []
    with open('ha.conf', 'r', encoding='utf-8') as f:   # 一行一行读取文件内容
        flag = False
        for line in f:
            if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                flag = True
                continue
            if flag and line.strip().startswith("backend"):     # 碰到下一个 backend 结束
                flag = False
                break
            if flag and line.strip():
                result.append(line.strip())     # 追加到列表
    return result

# 增加 backend 或者 backend 的记录值
def add(backend, record):
    record_list = fetch(backend)
    # backend 没有在ha.conf 文件里面，直接添加信息到文件
    if not record_list:
        with open('ha.conf', 'r') as old, open("new.conf", 'w') as new:
            for line in old:
                new.write(line)
            new.write("\nbackend " + backend + "\n")
            new.write(" " * 8 + record + "\n")
    else:
        # backend 存在，record 也存在
        if record in record_list:
            with open('ha.conf', 'r') as old ,open("new.conf", 'w') as new:
                for line in old:
                    new.write(line)
        # backend 存在，record 不存在
        else:
            record_list.append(record)
            with open('ha.conf','r') as old, open('new.conf', 'w') as new:
                flag = False
                for line in old:
                    if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                        flag = True
                        new.write(line)
                        for new_line in record_list:
                            new.write(" " * 8 + new_line + "\n")
                        continue
                    if flag and line.strip().startswith("backend"):
                        flag = False
                        new.write(line)
                    if line.strip() and not flag:
                        new.write(line)
xsy = "www.xsy.me"
rd  = "server 45.56.86.136 weight 20 maxconn 30"

add(xsy, rd)
