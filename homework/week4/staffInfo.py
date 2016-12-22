#!/usr/bin/env python3
# Author: shaoyan

import sys
"""
员工信息处理
"""

# 初始化数据，若 db 文件没有数据，可以调用这个函数写入初始化数据
def init_data():
    a = ["1,Alex Li,22,13651054608,IT,2013-04-01","2,shao yan,20,13651054888,IT,2016-04-01"]
    with open('db', 'wt') as f:
        i = 1
        for item in a:
            if i > 1:       # 大于第1行，才插入换行符
                f.write("\n")
                f.write(item)
            else:
                f.write(item)
            i += 1

# 分析 sql 函数
def  sql_analyse(sql):
    """
    这个函数会拆分 sql 语句，拆分成：类型，字段，条件
    :return sql_anal_dict{} 返回分析后的字典
    """
    sql_anal_dict = {} # 存放分析后的数据
    sql_list = sql.split(" ")
    # 删除多余的空格
    for item in sql_list:
        if item == "":
            sql_list.remove(item)
    # 判断 sql 语句是否输入正确！
    check_list = ['select', 'SELECT', 'update', 'UPDATE', 'delete', 'DELETE', 'alter', 'ALTER']
    if sql_list[0] not in check_list:
        print("sql 语句错误！请重新输入！")
        return 0
    else:
        # sql 语句的类型
        sql_anal_dict["sql_type"] = sql_list[0]
        sql_ziduan = []     # sql 语句的字段
        sql_tiaojian = []   # sql 语句的条件

        # 获取字段
        if "from" in sql_list:
            i = sql_list.index("from")
        elif "SET" in sql_list:
            i = sql_list.index("SET")
        else:
            print("sql 输入错误，请重新输入！")
            return 0
        for h in range(1, i):
            sql_ziduan.append(sql_list[h])
        sql_anal_dict["sql_ziduan"] = sql_ziduan

        # 获取条件
        j = sql_list.index("where") + 1
        for k in range(j, len(sql_list)):
            sql_tiaojian.append(sql_list[k])
        sql_anal_dict["sql_tiaojian"] = sql_tiaojian

        return sql_anal_dict


# 加载数据函数
def load_info():
    """
    这个函数是读取文件数据，返回一个字典
    :return: info_dict 数据字典
    """
    # 读取数据，存成列表
    dict_value = []     # 后面用来存入字典的值
    with open('db', 'r') as f:
        info = f.read()
        info_list = info.split("\n")  # 按照换行符拆分，存成列表

    for item in info_list: # 将列表的元素也拆分成列表
        a = item.split(',')
        dict_value.append(a)   # 将列表作为元素，追加到另一个列表。目的是：将每一行数据，存成一个子列表

    # 将列表的数据存到字典
    info_dict = {}
    dict_key = ['name', 'age', 'phone', 'dept', 'enroll_date']   # 数据信息字段。stuff_id 字段，用自增数字。
    for i in range(len(dict_value)):   # 用 i 作为 stuff_id
        info_dict[i] = dict.fromkeys(dict_key, None)  # 给字典初始化key，值默认为None

    j = 0   # stuff_id
    for item in dict_value:    # 遍历列表，将值赋给字典
        info_dict[j]['name'] = item[1]   # 给每个字段赋值
        info_dict[j]['age'] = int(item[2])
        info_dict[j]['phone'] = item[3]
        info_dict[j]['dept'] = item[4]
        info_dict[j]['enroll_date'] = item[5]
        j += 1
    return info_dict


# 查询信息
def check_info(argx):
    pass

# 增加新员工信息
def add_stuff():
    pass


# 修改员工信息
def update_info():
    pass

# 删除员工信息
def delete_info(stuff_id):
    pass

def help_info():
    help_info = '''
1.可以输入类似以下3行sql，进行查询信息：
    select name,age from staff_table where age > 22
    select  * from staff_table where dept = "IT"
    select  * from staff_table where enroll_date like "2013"
2.可以输入类似下面这行sql，进行更新信息：
    UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
3.可以输入类似以下这行，删除信息：
    delete staff_id = 1 from staff_table
4.输入 all 查看所有信息
    '''
    print(help_info)

def execute_sql(sql_anal):
        # 查询
        if sql_anal["sql_type"] == "select" or sql_anal["sql_type"] == "SELETE":
            print("我调用了")
            check_info(sql_anal)

        # 添加员工
        elif sql_anal["sql_type"] == "alter" or sql_anal["sql_type"] == "ALTER":
            add_stuff()

        # 修改、更新
        elif sql_anal["sql_type"] == "update" or sql_anal["sql_type"] == "UPDATE":
            update_info(sql_anal)

        # 删除
        elif sql_anal["sql_type"] == "delete" or sql_anal["sql_type"] == "DELETE":
            delete_info(sql_anal)
        else:
            pass

if __name__ == '__main__':
    exit_flag = False
    while exit_flag is not True:
        sql = input("输入 sql 语句进行操作\n输入 h 查询帮助，输入 q 退出\n请输入：")
        if sql == "h":
            help_info()
        elif sql == "":
            print("输入错误，请重新输入！")
        elif sql == "q":
            print("bye bye!")
            exit_flag = True
        else:
            sql_anal = sql_analyse(sql)
            if sql_anal != "":
                execute_sql(sql_anal)





