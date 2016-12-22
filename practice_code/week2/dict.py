#!/usr/bin/env python3
# Author: shaoyan

"""
字典
"""

id_db ={
    1234:{
        'name': "shaoyan",
        'age': 22,
        'addr': "gz"
    },
    1235:{
        'name': "alex",
        'age': 33,
        'addr': "beijing"
    }

}

id_db2= {
    1236:{
        'name': "stu1",
        'age': 23,
        'addr': "shanghai"
    }
}

id_db.update(id_db2)


# print(id_db)

# print(id_db.items())

for item in id_db:
    print(item)

for key in id_db:      # 取 key 值
    print(key, id_db[key])  # 取值
