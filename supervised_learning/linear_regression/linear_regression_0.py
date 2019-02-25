#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: linear_regression_0.py

import numpy as np
import matplotlib.pyplot as plt

__author__ = 'yasaka'

# 这里相当于是随机X维度X1，rand是随机均匀分布,数据的取值范围为[0, 1)
# np.random.rand(3,2)  这里生成二维的数据，数据示例如下
# array([[ 0.14022471,  0.96360618],  #random
#      [ 0.37601032,  0.25528411],  #random
#      [ 0.49313049,  0.94909878]]) #random

# 这里是生成一维的数据，np.random.rand(100, 1)的结果是100个范围是[0, 1)的一维数组
# [ [0.33], [0.423], ... , [0.211]]  数组长度100
# 2* np.random.rand(100, 1) 的范围是 [0, 2)
X = 2 * np.random.rand(100, 1)

# 人为的设置真实的Y一列，np.random.randn(100, 1)是设置error，randn是标准正太分布
y = 4 + 3 * X + np.random.randn(100, 1)
# 整合X0和X1, 为什么要整合这2项
# Y = W0*X0 + W1*X1
# 这里用到的方法c_意思是combine的意思，是连接前后两个向量，扩展更多的列。
X_b = np.c_[np.ones((100, 1)), X]
print(X_b)

# 常规等式求解theta
# linalg 是线性代数的工具包
# inv 是inverse的缩写，是对x求逆也就是矩阵x的-1
# 西塔 = (Xt . X )-1 . Xt . Y  这个方程式，详细见尚学堂的教程
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print(theta_best)

# 创建测试集里面的X1
X_new = np.array([[0], [2]]) 
X_new_b = np.c_[(np.ones((2, 1))), X_new]
print(X_new_b)
y_predict = X_new_b.dot(theta_best)
print(y_predict)

plt.plot(X_new, y_predict, 'r-')
plt.plot(X, y, 'b.')
plt.axis([0, 2, 0, 15])
plt.show()



