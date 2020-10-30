#!/usr/bin/env python 
# coding:utf-8 
# @Time :2020/10/28 3:22 下午
# @File :fib_cycle.py

'''
斐波那契数列F0=0,F1=1,...,Fn = F(n-1) + F(n-2),
目标是输出前n项的数列，即F0——Fn，一共n+1个数。
'''

def fib_cycle(n):      # n表示生成到第0-n项斐波那契数列，即生成前n+1个数字
    cycle_result = []  # 创建一个列表用来存储该数列
    f0, f1 = 0,1    # 保存前两个数字，第0项和第1项初始化
    # 满足循环条件，就继续下面的运算，如果n<=0，即默认输出f0=0
    while n > 0:
        cycle_result.append(f0)
        f0, f1 = f1, f0 + f1
        n -= 1          #循环次数逐渐减少
    cycle_result.append(f0)
    return cycle_result

if __name__ == "__main__":
    n = int(input("Please enter an integer:"))
    fib = fib_cycle(n)
    print(fib)

