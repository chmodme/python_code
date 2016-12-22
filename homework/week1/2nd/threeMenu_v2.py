#!/usr/bin/env python3
# Author: shaoyan

import json,sys

"""
三级菜单
1. 运行程序，输出第一级菜单
2. 选择一级菜单某项，输出二级菜单，
    同理输出三级菜单
3. 菜单数据保存在文件中
"""

# 初始化数据。若 menu.json 文件已经有数据，则不用重复初始化
data = {
    "广东省":{
        "广州市":{
            "番禺区":[
                "长隆水上乐园","广州大学城"
            ],
            "天河区":[
                "天河体育馆"
            ]
        },
        "深圳市":{
            "南山区":[
                "深圳科技园","西丽大学城"
            ],
            "宝安区":[
                "世界之窗"
            ]
        }
    },
    "福建省":{
        "厦门市":{
            "集美区":[
                "集美大学"
            ],
            "思明区":[
                "鼓浪屿"
            ]
        },
        "泉州市":{
            "丰泽区":[
                "黎明大学","泉州森林公园"
            ]
        }

    }


}

# 将字典数据，用 json 写到文件
# with open("menu.json", 'w') as f:
#    json.dump(data, f)

# 读取 json 数据函数
def get_data():
    with open("menu.json", 'r') as j:
        menu = json.load(j)
    return menu

# 定义函数：
# 打印一级菜单函数
def print_first_menu(menu):
    print("一级菜单省份有：")
    for k in menu.keys():
        print(k)

# 打印二级菜单函数
def print_second_menu(menu, sheng):
    print("%s二级菜单市有："%sheng)

    for l in menu[sheng].keys():
        print(l)

# 打印三级菜单函数
def print_third_menu(menu,sheng,shi):
    print("%s%s三级级菜单市有："%(sheng,shi))
    for m in menu[sheng][shi].keys():
        print(m)

# 程序开始入口
# 获取数据
menu = get_data()
print(menu)
for i in range(4):
    if i < 3:
        print_first_menu(menu)
        # 接收一级菜单输入
        sheng = input("输入省份名称查看省份下级市，输入q退出：")
        if sheng in menu.keys():
            for j in range(4):
                print_second_menu(menu,sheng)
                shi = input("输入市的名称查看下级区，输入b返回一级，输入q退出：")
                if shi in menu[sheng].keys():
                    print_third_menu(menu,sheng,shi)
                    for k in range(4):
                        qu = input("输入区域名称查看区域的景点，输入b返回二级，输入q退出：")
                        if qu in menu[sheng][shi].keys():
                            print("%s的景点特色有："%qu)
                            for l in menu[sheng][shi][qu]:
                                print(l)
                                sys.exit("三级菜单浏览完毕！程序退出")
                        elif qu == "b":
                            break
                        elif qu == "q" or k > 3:
                            sys.exit("程序退出")
                        else:
                            print("输入错误，请重新输入！")
                elif shi == "b":
                    break
                elif shi == "q" or j >3:
                    sys.exit("程序退出！")
                else:
                    print("输入错误，请重新输入！")
        elif sheng == "q":
            sys.exit("程序退出！")
        else:
            print("输入错误，请重新输入")
    else:
        print("输入超过3次，程序退出！")
        sys.exit()
