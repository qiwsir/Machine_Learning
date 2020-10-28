#!/usr/bin/env python 
# coding:utf-8 
# @Time :2020/10/24 10:32 上午
# @File :guess_number.py

# 导入产生随机数的库
import random

# 由计算机生成一个100以内(1-99)的随机整数，用户不可见
guess_num = random.randint(1, 100)
# 由用户输入一个数字，代表猜数字的上限次数
guess_chance = int(input("Please enter the number of guess chances."))

''' 定义一个猜数字游戏的函数,
    可以通过修改参数进行不同范围的猜数字游戏'''

def guess_number_game(guess_num, guess_chance):
    sum = 0   # 用来记录已经猜测的次数
    # 提示开始游戏
    print("Guess the number game begins(1-100):")

    # 循环开始，猜的数字在规定的范围内
    while sum < guess_chance:
    # for i in range(guess_chance):   #表示次数可以从0开始
        sum += 1
        try:     # if not y.isdigit():print("please enter an int")
            guess = int(input("Please enter the number:"))
        # 如果猜的数据不在规定范围内，则提示错误，并将该次猜测数记录进去
            if guess < 0 or guess >= 100:
                print("You must guess a number between 0-99!")

        # 如果猜的数据小于设定数据，则输出数据偏小，并使得猜测次数+1
            elif guess < guess_num:
                print("Your guess is small！")

        # 如果猜的数据大于设定数据，则输出数据偏大，并使得猜测次数+1
            elif guess > guess_num:
                print("Your guess is big！")

        # 如果猜的数据等于设定数据，则输出"你猜对了"，并使得猜测次数+1
            elif guess == guess_num:
                print("Your are right!")
                print("You have guessed " + str(sum) + " times！")
                break
        # 设置异常，如果输入的不是整数，则跳出异常
        except ValueError:
            print("Input Error,please enter an integer!")
            continue

    # 如果猜测次数超过限定次数，则输出正确答案
    if sum == guess_chance:
        print(f"You have guessed {sum} times! The correct answer is :{guess_num} !")

guess_number_game(guess_num,guess_chance) # 调用函数

