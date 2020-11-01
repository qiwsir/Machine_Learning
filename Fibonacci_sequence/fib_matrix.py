# coding:utf-8
# @Time :2020/10/28 3:43 下午
# @File :fib_matrix.py

import numpy as np   #导入numpy，便于生成矩阵

'''
斐波那契数列第n+1个数字等价于
矩阵[[1, 1],[1, 0]]的n次方中
位于左上角[0][0]位置上的数字
'''

# 定义一个矩阵运算函数
def fib_matrix_method(n):   # n代表第n+1个数
    matrix = np.mat([[1, 1],[1, 0]])   # 用np.mat生成一个矩阵
    return pow(matrix, n)     # 计算该矩阵的n次方，用pow实现

# 定义一个函数，用于输出矩阵左上角的数字作为斐波那契序列的每一项
def fib_matrix(n):
    result_matrix = [0]   # 第0项默认输出0
    for i in range(n):
        result_matrix.append(np.array(fib_matrix_method(i))[0][0])
    return result_matrix

if __name__ == "__main__":
    n = int(input("Please enter an integer:"))
    fib = fib_matrix(n)   #调用函数
    print(fib)