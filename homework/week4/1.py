#!/usr/bin/env python3
# Author: shaoyan

"""

"""

list_a = [['yan', '20', '2'], ['ming', '30', '4']]
list_b = ['name','age', 'level']

dict_a = {}

for i in range(len(list_a)):
    dict_a[i] = dict.fromkeys(list_b)
print(dict_a)

j = 0
for item in list_a:
    dict_a[j]['name'] = item[0]
    dict_a[j]['age'] = item[1]
    dict_a[j]['level'] = item[2]
    j += 1

print(dict_a)

else:





