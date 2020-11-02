# coding:utf-8
# @Time :2020/10/28 3:39 下午
# @File :fib_iterator.py


'''
使用迭代器的方法生成斐波那契数列（生成0-n项）
首先定义一个迭代器的类
'''

class fib_iterator():
    def __init__(self, n):
        self.n = n      # 定义斐波那契数列第n项（即共生成F0--Fn项数列）
        self.f0 = 0     # 定义斐波那契数列第0项（第一个数字）
        self.f1 = 1     # 定义斐波那契数列第1项（第二个数字）
        self.index = 0  # 记录生成数字的下标   ## 可以精简掉这个

    def __iter__(self):    # 定义迭代器对象
        return self

    def __next__(self):    # 定义next方法来生成下一个数字
        if self.index < self.n:
            self.f0, self.f1 = self.f1, self.f0 + self.f1
            result = self.f0
            self.index += 1
            return result
        else:
            raise StopIteration  # 在循环对象穷尽所有元素时进行报错


if __name__ == "__main__":
    n = int(input("Please enter an integer:"))
    result_iter = [0]   # n小于等于0时，只输出第0项数字
    f = fib_iterator(n)
    print(result_iter + list(f))
