#!/usr/bin/env python 
# coding:utf-8 
# @Time :2020/10/28 3:33 下午
# @File :fib_yield.py


# 定义一个生成器
def fib_yield(n):
    f0, f1 = 0, 1   # 记录前两个数字
    if n <= 0:      # 如果n小于等于0，都只输出第0项数字
        yield 0
    else:
        while n > 0:
            yield f0   # 不断生成下一个斐波那契数列
            f0, f1 = f1, f0 + f1
            n -= 1
        yield f0  # 生成最后第n项（第n+1个数）

if __name__ == "__main__":
    n = int(input("Please enter an integer:"))
    yield_result = []
    for i in fib_yield(n):     # 把生成器中的数字依次输出
        yield_result.append(i)
    print(yield_result)