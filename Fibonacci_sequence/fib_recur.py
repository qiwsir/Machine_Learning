# coding:utf-8
# @Time :2020/10/28 3:51 下午
# @File :fib_recur.py

'''
递归生成斐波那契数列是效果最差的方法！
'''

#定义用递归方法生成数列的函数
def fib_recur_method(n):
    if n <= 1:  # 第0项和第1项是它本身
        return n
    else:  # 反之则返回前两个数的和
        return fib_recur_method(n - 1) + fib_recur_method(n - 2)

# 将整个数列以列表的形式输出
def fib_recur(n):
    recur_result = []
    for i in range(0, n + 1):  # 斐波那契数列是从第0项开始的
        recur_result.append(fib_recur_method(i))
    return recur_result

if __name__ == "__main__":
    n = int(input("Please enter an integer:"))
    fib = fib_recur(n)
    print(fib)