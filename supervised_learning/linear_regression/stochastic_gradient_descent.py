#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: stochastic_gradient_descent.py

import numpy as np

__author__ = 'yasaka'

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
X_b = np.c_[np.ones((100, 1)), X]
# print(X_b)

n_epochs = 500   # 学习轮数，随机梯度下降通过增加轮数，来提高得到最优解的概率
t0, t1 = 5, 50  # 用来计算学习率的超参数
m = 100   # 样本数量

def learning_schedule(t):
    """
    计算学习率
    :param t: 
    :return: 
    """
    return t0 / (t + t1)

# 1，初始化theta，w0...wn
theta = np.random.randn(2, 1)

for epoch in range(n_epochs):
    for i in range(m):
        # 随机获取一个下标值[0, m)
        random_index = np.random.randint(m)
        xi = X_b[random_index:random_index+1]
        yi = y[random_index:random_index+1]
        gradients = 2*xi.T.dot(xi.dot(theta) - yi)
        learning_rate = learning_schedule(epoch*m + i)
        theta = theta - learning_rate * gradients

print(theta)