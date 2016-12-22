#!/usr/bin/env python3
# Author: shaoyan

"""
猜数字！
"""
age = 24
counter = 0

for i in range(10):
    if counter < 3:
        guess_num = int(input("input your guess number:"))
        if guess_num == age:
            print("congratulations! you got it!")
            break
        elif guess_num > age:
            print("It's big, think smaller!")
        else:
            print("It's small, think big!")
    else:
        continue_confirm = input("do you want to continue because you are stupid:")
        if continue_confirm == 'y':
            counter = 0
            continue
        else:
            print("bye")
            break
    counter += 1