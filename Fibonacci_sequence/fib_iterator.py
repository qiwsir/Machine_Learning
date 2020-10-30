#!/usr/bin/env python 
# coding:utf-8 
# @Time :2020/10/28 3:39 下午
# @File :fib_iterator.py


# 定义一个迭代器的类
class fib_iterator():
    def __init__(self, n):
        self.n = n
        self.f0 = 0
        self.f1 = 1
        self.index = 0  # 记录生成数字的下标

    def __iter__(self):
        return self

    def __next__(self):
        # 生成下一个数字
        if self.index < self.n:
            self.f0, self.f1 = self.f1, self.f0 + self.f1
            result = self.f0
            self.index += 1
            return result
        else:
            raise StopIteration  # 在循环对象穷尽所有元素时进行报错


if __name__ == "__main__":
    n = int(input("Please enter an integer:"))
    result_iter = [0]
    f = fib_iterator(n)
    print(result_iter + list(f))
