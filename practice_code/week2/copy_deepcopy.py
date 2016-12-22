#!/usr/bin/env python3
# Author: shaoyan
import copy

"""

"""

name = ['alex', 'yan', 'jack', "rain", [1,2,3,4]]
name2 = name.copy()
name3 = copy.deepcopy(name)

name[4][1] = 22

print(name2)
print(name3)