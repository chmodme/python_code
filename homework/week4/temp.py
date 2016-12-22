#!/usr/bin/env python3
# Author: shaoyan
from collections import defaultdict

"""

"""
# a = ["1,Alex Li,22,13651054608,IT,2013-04-01", "2,shao yan,20,13651054888,IT,2016-04-01"]

# for item in a:
#    print(item)


ziduan = ['stuff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']

a = [['1', 'Alex Li', '22', '13651054608', 'IT', '2013-04-01'],['1', 'xiao ming', '22', '13651054608', 'IT', '2013-04-01']]


dict_tmp2 = {}

dict_tmp = dict.fromkeys(ziduan)

for i in range(len(a)):
    dict_tmp2[i] = dict_tmp
    dict_tmp2[i]['name'] = a[i][1]

print(dict_tmp2)

dict_tmp = dict.fromkeys(ziduan)

for i in range(len(a)):
    dict_tmp2[i] = dict_tmp
    dict_tmp2[i]['name'] = a[i][1]

print(dict_tmp2)

for item in data_info_list:
    temp = item.split(",")
    print(temp)
    for item2 in temp:
        print(item2)

        stuff_id = int(temp[0])
        data_dict[stuff_id]["name"] = temp[1]
        data_dict[stuff_id]["age"] = temp[2]
        data_dict[stuff_id]["phone"] = temp[3]
        data_dict[stuff_id]["dept"] = temp[4]
        data_dict[stuff_id]["enroll_date"] = temp[5]
        print(data_dict)