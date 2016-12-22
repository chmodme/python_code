#!/usr/bin/env python3
# Author: shaoyan

"""
装饰器练习
"""

import time

def timer(func):
    def warper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return warper

@timer
def test1():
    time.sleep(3)
    print('in the test1')

test1()
