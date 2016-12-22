#!/usr/bin/env python3
# Author: shaoyan

import json

"""
临时测试文件

"""
# list1 = [12, 12, 1234, 23]
# print(list1)

# test json 带格式存储json
shop_data = {
    "手机": {
        "小米": {
            "小米5": {
                "price": 1500, "num": 10
            },
            "红米": {
                "price": 800, "num": 100
            }
        },
        "华为": {
            "meta 8": {
                "price": 3000, "num": 50
            }
        }
    },
    "笔记本电脑": {
        "联想": {
            "thinkpad x 1": {
                "price": 5000, "num": 300
            }
        },
        "华硕": {
            "华硕R556UJ": {
                "price": 3999, "num": 10
            }
        }
    }

}


# 写法一：
with open("lesson_code.json", 'w') as f:
    json.dump(shop_data, f, indent=1)

# 写法二：
json.dump(shop_data, open("lesson_code.json", 'w'), indent=1)
