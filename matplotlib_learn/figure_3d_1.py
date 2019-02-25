import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt  # ddf

from matplotlib import cm      #里面有很多颜色映射表；
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter

def fig_3d_1():
    mpl.rcParams['legend.fontsize'] = 10  # 设置图示的字体大小；

    fig = plt.figure()
    ax = fig.gca(projection='3d')  # 它表示得到一个3D的axes,
    # 也可以用代码： ax = fig.add_subplot(111, projection='3d')
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(0, 4, 100)
    r = z
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax.plot(x, y, z, label='parametric curve')  # 直接把x, y, z 三者对应的坐标的点传进去了呀
    ax.legend()  # 显示图示；

    plt.show()


def fig_3d_2():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)  # 创建X——Y平面表格；
    R = np.sqrt(X ** 2 + Y ** 2)  # 计算每点的高度；
    Z = np.cos(R)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)

    ax.zaxis.set_major_locator(LinearLocator(10))  # 设置z轴的坐标为线性的，且有10个坐标标记啦；
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  # 应该设置了这个z轴坐标的显示格式啦；
    fig.colorbar(surf, shrink=.5, aspect=5)  # 设置那个颜色带的大小；

    plt.show()

def fig_3d_3():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-5, 5, 0.25)
    xlen = len(X)
    Y = np.arange(-5, 5, 0.25)
    ylen = len(Y)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    colortuple = ('y', 'b')
    colors = np.empty(X.shape, dtype=str)
    for y in range(ylen):
        for x in range(xlen):
            colors[x, y] = colortuple[(x + y) % len(colortuple)]

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=colors,
                           linewidth=0, antialiased=False)

    ax.set_zlim3d(-1, 1)
    ax.w_zaxis.set_major_locator(LinearLocator(6))

    plt.show()

def fig_3d_4():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    def cc(arg):  # 它的作用就是改改颜色啦，把颜色的A值 改为0.5，（RGBA是什么看百度，它代表了4个值，然后呢，函数把传入的颜色的lapha值变为0.5）
        return colorConverter.to_rgba(arg, alpha=0.5)

    xs = np.arange(0, 10, 0.4)
    verts = []
    zs = [0.0, 1.0, 2.0, 3.0]
    for z in zs:  # 生成x值、y值对。
        ys = np.random.rand(len(xs))  # 产生在0－1之间均匀分布的一定个数的随机数；
        ys[0], ys[-1] = 0, 0
        verts.append(list(zip(xs, ys)))  # 函数zip()的作用就是把传放的xs, ys一维数组变为[(xs0, ys0),  (xs1, ys1), (xs1, ys1),   ……]

    poly = PolyCollection(verts, facecolors=[cc('r'), cc('g'), cc('b'),
                                             cc('y')])
    poly.set_alpha(0.7)  # 设置透明度；
    ax.add_collection3d(poly, zs=zs, zdir='y')  # 把z轴方向变为y轴方向；

    ax.set_xlabel('X')
    ax.set_xlim3d(0, 10)
    ax.set_ylabel('Y')
    ax.set_ylim3d(-1, 4)
    ax.set_zlabel('Z')
    ax.set_zlim3d(0, 1)

    plt.show()

fig_3d_4()