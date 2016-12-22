import time

__author__ = "yan"

def timer(func):
    def deco():
        start_time = time.time()
        func()  # run test1()
        stop_time = time.time()
        print('run time is %s' %(stop_time-start_time))
    return deco

@timer  # test1 = timer(test1)
def test1():
    time.sleep(3)
    print('in the test1')

@timer  # test2 = timer(test2)
def test2():
    time.sleep(3)
    print('in the test2')


