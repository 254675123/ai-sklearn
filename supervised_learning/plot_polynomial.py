import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.stats import norm
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

''' 
数据生成 
norm为正态分布，数据分布的函数有下面一些方法：
正态分布norm.mean(), norm.std(), norm.var() 的默认结果(0.0, 1.0, 1.0)

rvs:随机变量（就是从这个分布中抽一些样本）
pdf：概率密度函数。
cdf：累计分布函数
sf：残存函数（1-CDF）
ppf：分位点函数（CDF的逆）
isf：逆残存函数（sf的逆）
stats:返回均值，方差，（费舍尔）偏态，（费舍尔）峰度。
moment:分布的非中心矩。
'''
x = np.arange(0, 1, 0.002)
# 产生了一个正态分布变量，其期望，即loc=0, 样本数量size=500
# 可以使用np.mean方法看期望均值，np.mean(norm.rvs(0, size=500))
# 所有连续分布可以操纵loc以及scale参数调整分布的location和scale属性。
# 作为例子， 标准正态分布的location是均值而scale是标准差。
# 这里产生的都是杂质数据
y = norm.rvs(0, size=500, scale=0.1)
y = y + x ** 2

''' 
均方误差根 
mean-squared-error
'''
def rmse(y_test, y):
    return sp.sqrt(sp.mean((y_test - y) ** 2))


''' 与均值相比的优秀程度，介于[0~1]。0表示不如均值。
1表示完美预测.这个版本的实现是参考scikit-learn官网文档  
'''
def R2(y_test, y_true):
    return 1 - ((y_test - y_true) ** 2).sum() / ((y_true - y_true.mean()) ** 2).sum()


''' 这是Conway&White《机器学习使用案例解析》里的版本 '''
def R22(y_test, y_true):
    y_mean = np.array(y_true)

    y_mean[:] = y_mean.mean()
    return 1 - rmse(y_test, y_true) / rmse(y_mean, y_true)

# s : scalar or array_like, shape (n, ), optional
# size in points^2. Default is rcParams['lines.markersize'] ** 2.
# c : color, sequence, or sequence of color, optional, default: ‘b’
# c can be a single color format string,
# or a sequence of color specifications of length N,
# or a sequence of N numbers to be mapped to colors using the cmap
# and norm specified via kwargs (see below). Note that c should not be a
# single numeric RGB or RGBA sequence because that is indistinguishable
# from an array of values to be colormapped. c can be a 2-D array in which
# the rows are RGB or RGBA, however, including the case of a single row to
# specify the same color for all points.
# marker : MarkerStyle, optional, default: ‘o’
plt.scatter(x, y, s=5)
degree = [1, 2, 100]
y_test = []
y_test = np.array(y_test)

# 使用sklearn.preprocessing.PolynomialFeatures来进行特征的构造。
# 它是使用多项式的方法来进行的，如果有a，b两个特征，
# 那么它的2次多项式为（1,a,b,a^2,ab, b^2），这个多项式的形式是使用poly的效果。
# PolynomialFeatures有三个参数
# 1. degree：控制多项式的度
# 2. interaction_only： 默认为False，如果指定为True，那么就不会有特征自己和自己结合的项，
#   上面的二次项中没有a^2和b^2。
# 3. include_bias：默认为True。如果为True的话，那么就会有上面的 1那一项。
for d in degree:
    # 这里的LinearRegression没有使用正则化，所以degree=100的时候
    # 会产生过拟合的现象，为了避免这种现象，可以使用正则化方法
    # L1正则的lasso，L2正则的Ridge，L1+L2的Elastic Net

    # clf = Pipeline([('poly', PolynomialFeatures(degree=d)),
    #                 ('linear', LinearRegression(fit_intercept=False))])
    clf = Pipeline([('poly', PolynomialFeatures(degree=d)),
                    ('linear', linear_model.Ridge())])
    clf.fit(x[:, np.newaxis], y)
    y_test = clf.predict(x[:, np.newaxis])

    print(clf.named_steps['linear'].coef_)
    print('rmse=%.2f, R2=%.2f, R22=%.2f, clf.score=%.2f' %
          (rmse(y_test, y),R2(y_test, y),R22(y_test, y),clf.score(x[:, np.newaxis], y)))
    plt.plot(x, y_test, linewidth=2)

    plt.grid()
    plt.legend(['1', '2', '100'], loc='upper left')
    plt.show()

