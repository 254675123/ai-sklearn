import numpy as np
"""
np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等，类似于pandas中的concat()。

np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()。
"""
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.c_[a,b]

print(np.r_[a,b])
print(c)
print(np.c_[c,a])