#!/usr/bin/env python3
# Author: shaoyan
import json,sys

"""
购物车：
1. 商品信息- 数量、单价、名称               # 使用字典存储
2. 用户信息- 帐号、密码、余额               # 使用字典存储
3. 用户可充值                             # 用户金额 = 原有 + 充值
4. 购物历史信息                           # 购买后存储购买信息：存用户名，购买的商品，金额等信息
5. 允许用户多次购买，每次可购买多件          # 循环购买
6. 余额不足时进行提醒                      # 判断支付金额是否大于用户金额
7. 用户退出时 ，输出当次购物信息             # 打印当次购物信息
8. 用户下次登陆时可查看购物历史              # 读取购物历史
9. 商品列表分级显示                        # 读取商品信息
"""

# 初始化数据：若文件为空，则修改flag，进行初始化
chu_shi_hua_flag = False
while chu_shi_hua_flag:
    # 用户信息字典，使用 json 存储到文件
    user_data = {
        "小明":{
            "password": "123456", "balance": 10000
        },
        "小强":{
            "password": "123456", "balance": 10000
        }
    }

    # 商品信息字典，使用 json 存储到文件
    shop_data = {
        "手机":{
            "小米":{
                "小米5":{
                    "price": 1500,"num": 10
                },
                "红米":{
                    "price": 800, "num": 100
                }
            },
            "华为":{
                "meta 8":{
                    "price": 3000, "num": 50
                }
            }
        },
        "笔记本电脑":{
            "联想":{
                "thinkpad x 1": {
                    "price": 5000, "num": 300
                }
            },
            "华硕":{
                "华硕R556UJ":{
                    "price": 3999, "num": 10
                }
            }
        }

    }

    # 用户订单字典，使用 json 存储到文件
    order_data = {
        "小明":{
            "1":{
                "小米5": {
                    "price": 1500, "num": 1, "sum":1500
                },
                "meta 8": {
                    "price": 3000, "num": 2, "sum":6000
                },
                "sum_total": 7500
            },
            "2": {
                "thinkpad x 1": {
                    "price": 5000, "num": 2, "sum": 10000
                },
                "小米5": {
                    "price": 1500, "num": 2, "sum":3000
                },
                "sum_total": 13000
            }
        },
        "小强":{
            "1": {
                "meta 8": {
                    "price": 3000, "num": 1,"sum":3000
                },
                "华硕R556UJ": {
                    "price": 3999, "num": 1,"sum":3999
                },
                "sum_total": 6999
            },
            "2": {
                "thinkpad x 1": {
                    "price": 5000, "num": 1, "sum": 5000
                },
                "meta 8": {
                    "price": 3000, "num": 2, "sum": 6000
                },
                "sum_total":11000
            }
        }
    }

    # 当前购物车字典，购买时候，将购物车信息，追加到用户订单信息，退出时候，打印购物车

    # 写入json文件
    with open("user.json", 'w') as u:
        json.dump(user_data, u)

    with open("shop.json", 'w') as s:
        json.dump(shop_data, s)

    with open("order.json", 'w') as o:
        json.dump(order_data, o)

    print("初始化完成！\n")
    break

# 功能程序部分
# 加载数据：
with open("user.json", 'r') as u:
    user = json.load(u)
with open("shop.json", 'r') as s:
    shop = json.load(s)
with open("order.json", 'r') as o:
    order = json.load(o)

# 定义函数
# 用户登录函数
def login():
    i = 0
    while True:
        if i < 3:
            input_user = input("请输入你的用户名：")
            input_pwd = input("请输入你的密码：")
            if input_user in user.keys():
                if user[input_user]["password"] == str(input_pwd):
                    print("登录成功\n")
                    return input_user
                else:
                    print("用户名或者密码错误！")
                    i += 1
            else:
                print("用户名或者密码错误！")
                i += 1
        else:
            print("尝试次数超过3次，请1个小时后再尝试！")
            break

# 获取用户购物历史信息 函数
def get_user_order(login_u):
    print("%s的历史订单信息："%login_u)
    for key in order[login_u]:
        print("订单：",key)    # 打印订单名称
        for key2 in order[login_u][key]:    # 打印订单中的商品信息
            if key2 != "sum_total":
                print("购买了商品：%s ，%d件，价格是%d，共花费%d" %(key2, order[login_u][key][key2]['num'], order[login_u][key][key2]['price'],order[login_u][key][key2]['sum']))
        print("订单总金额是：%d\n" % order[login_u][key]['sum_total'])


def recharge():
    print("当前用户剩余金额为：%d" % user[login_user]['balance'])
    charge = int(input("请输入充值金额："))
    user[login_user]['balance'] += charge   # 修改用户余额
    # 充值完成，写入文件，保存起来
    with open("user.json", 'w') as w_u:
        json.dump(user, w_u)
    print("充值完成！\n")


# 商品分级显示，提供购买 函数：
def shopping(who):
    # 显示商品信息：
    shop_list = []  # 定义一商品列表，存商品名称
    shop_price = []  # 定义一个商品价格列表，存商品价格
    shop_num = []  # 定义一个商品剩余列表，存商品剩余数量
    shop_car_data = {} # 定义一个购物车字典
    i = 0
    print("\n当前所有商品：")
    for key in shop:
        print("%s" % key)
        for key2 in shop[key]:
            print("\t%s" % key2)
            for key3 in shop[key][key2]:
                shop_list.append(key3)  # 将商品名称追加到列表，方便购买
                shop_price.append(shop[key][key2][key3]['price'])
                shop_num.append(shop[key][key2][key3]['num'])
                print("\t\t商品编号：%d ：%s，价格：%s，剩余数量：%s" % (i,key3,shop[key][key2][key3]['price'],shop[key][key2][key3]['num']))
                i += 1
    shop_stop_flag = False
    shop_sum_total = 0  # 所有购物的总金额
    # 获取购买信息：
    while shop_stop_flag is not True:
        shop_bian_hao = int(input("请输入商品编号，进行购买："))
        shop_count = int(input("请输入购买数量："))
        if shop_bian_hao is not None and shop_count is not None and shop_bian_hao < len(shop_list):
            if shop_count < shop_num[shop_bian_hao]:
                shop_sum = shop_price[shop_bian_hao]*shop_count  # 一次循环购买的金额
                if shop_sum < user[who]['balance']:
                    user[who]['balance'] -= shop_sum    # 扣取金额
                    # 追加商品信息到购物车
                    shop_name = shop_list[shop_bian_hao]    # 购买的商品名称
                    shop_pri = shop_price[shop_bian_hao]    # 购买的商品价格
                    shop_n = shop_count                     # 购买的商品数量
                    shop_car_data[shop_name] = {
                        'price': shop_pri,
                        'num': shop_n,
                        'sum': shop_sum
                    }
                    shop_sum_total += shop_sum  # 当前所有购物的总金额
                    shop_car_data["sum_total"] = shop_sum_total
                    print("购买成功")
                else:
                    print("用户余额不足！")
                    temp = input("若充值请输入1，输入其他或回车将退出购买：")
                    if temp == "1":
                        recharge()
                    else:
                        break
            else:
                print("商品剩余数量不足！%s 剩余：%d 件,请重新购买！"%(shop_list[shop_bian_hao],shop_num[shop_bian_hao]))
        else:
            print("输入错误，请重新输入！")
        # 完成购买或是退出购买：
        input_quit = input("输入q or quit 退出购买，回车继续购买：")
        if input_quit == "q" or input_quit == "quit":
            # 打印本次购买信息：
            print("\n购买信息：")
            for key in shop_car_data:
                if key != "sum_total":
                    print("购买的商品：%s，价格：%d，数量：%d，总共花费：%d" % (key,shop_car_data[key]['price'],shop_car_data[key]['num'],shop_car_data[key]['sum']))
            print("\n当次购买花销的总金额：%d，当前用户账号剩余金额为：%d" % (shop_car_data["sum_total"], user[who]['balance']))

            # 将购物车信息，追加到订单字典
            order_num = len(order[who]) + 1 # 设置订单编号
            order[who][order_num] = shop_car_data
            # 将订单信息写入文件，方便下次读取
            with open("order.json", 'w') as w_o:
                json.dump(order,w_o)
            # 将用户信息，存入文件，方便下次读取，余额已经在购买的时候减去，只需写入保存即可。
            with open("user.json", 'w') as w_u:
                json.dump(user,w_u)
            break

# start
print("请先登录账号！")
# 用户登录，并获取登录的用户名
login_user = login()

# 打印用户历史订单
login_flat = False  # 用户登录标记

if login_user != "":
    login_flat = True
while login_flat:
            tmp = input("操作提示：\n1.进行充值\n2.进行购物\n3.查看用户历史订单\n请输入1或2或3,或输入q or quit 退出：")
            if tmp == "1":
                recharge()
            elif tmp == "2":
                shopping(login_user)
            elif tmp == "3":
                get_user_order(login_user)
            elif tmp =="q" or tmp == "quit":
                sys.exit("程序退出，88！")
            else:
                print("输入错误，请重新输入！")
