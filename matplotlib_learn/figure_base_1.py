import numpy as np
import matplotlib.pyplot as plt

def figure_split():
    plt.figure(1)  # 建立figure(1)
    plt.figure(2)  # 建立figure(2)
    # 当前图是figure2，下面的坐标都在figure2进行
    ax1 = plt.subplot(2, 1, 1)
    ax2 = plt.subplot(2, 1, 2)
    plt.sca(ax1)  # 切换到子图1
    plt.sca(ax2)  # 切换到子图2
    plt.figure(1)  # 切换到figure(1),它不是重建哦；

def fig_1():
    plt.figure()
    # range(5) 会生成一个range对象，默认start=0，step=1，这里的5就是end=5
    x = range(5)
    line = plt.plot(range(5))[0]  # plot函数返回的是一个列表,因为可以同时画多条线的哦;
    line.set_color('r')
    line.set_linewidth(2.0)
    plt.show()
    # ————————————  或者  ————————————
    plt.figure()
    line = plt.plot(range(5))[0]  # plot函数返回的是一个列表,因为可以同时画多条线的哦;
    line.set(color = 'g', linewidth = 2.0)
    plt.show()
    # ———————————— 或者 ————————————


    plt.figure()
    lines = plt.plot(range(5), range(5), range(5), range(8, 13))  # plot函数返回一个列表;
    plt.setp(lines, color='g', linewidth=2.0)  # setp函数可以对多条线进行设置的;
    plt.show()


def fig_2():
    # subplot(numRows, numCols, plotnum)
    for i, color in enumerate('rgbyck'):
        plt.subplot(321 + i, facecolor=color)
    plt.show()

def fig_3():
    fig = plt.figure(1)  # 创建了一个figure对象;

    # figure对象的add_axes()可以在其中创建一个axes对象,
    # add_axes()的参数为一个形如[left, bottom, width, height]的列表,取值范围在0与1之间;
    ax = fig.add_axes([0.1, 0.6, 0.3, 0.3])  # 我们把它放在了figure图形的上半部分，对应参数分别为：left, bottom, width, height;
    ax.set_xlabel('time')  # 用axes对象的set_xlabel函数来设置它的xlabel
    ax = fig.add_axes([0.6, 0.6, 0.3, 0.3])
    line = ax.plot(range(5))[0]  # 用axes对象的plot()进行绘图,它返回一个Line2D的对象;
    line.set_color('r')  # 再调用Line2D的对象的set_color函数设置color的属性;
    plt.show()

def fig_4():
    plt.plot([1, 2, 3], [4, 5, 6])
    axis = plt.gca().xaxis
    ticklocs = axis.get_ticklocs()  # 得到刻度位置;
    ticklabels = axis.get_ticklabels()  # 得到刻度标签;
    ticklines = axis.get_ticklines()  # 得到刻度线;
    ticklines2 = axis.get_ticklines(minor=True)  # 得到次刻度线; 举个例子:就像我们的尺子上的厘米的为主刻度线,毫米的为次刻度线;
    for label in axis.get_ticklabels():
        label.set_color('red')  # 设置每个刻度标签的颜色;
        label.set_rotation(45)  # 旋转45度;
        label.set_fontsize(16)  # 设置字体大小;
    for line in axis.get_ticklines():
        line.set_color('green')
        line.set_markersize(15)  # 设置刻度线的长短;
        line.set_markeredgewidth(3)  # 设置线的粗细
    plt.show()

def fig_5():
    plt.figure()
    ax = plt.plot(range(4))

    plt.text(0.5, 0.5,'hello, world', color = 'bule')   #还可以写更多参数的；
    plt.figtext(0.1, 0.8, "i am in figure', color = 'green'")
    plt.show()

def fig_6():
    plt.figure(1)  # 调用figure函数创建figure(1)对象,可以省略,这样那plot时,它就自动建一个啦;

    t = np.arange(0.0, 2.0, 0.1)
    s = np.sin(2 * np.pi * t)
    plt.plot(t, s, 'r--o', label='sinx')

    plt.legend()  # 显示右上角的那个label,即上面的label = 'sinx'
    plt.xlabel('time (s)')  # 设置x轴的label，pyplot模块提供了很直接的方法，内部也是调用的上面当然讲述的面向对象的方式来设置；
    plt.ylabel('voltage (mV)')  # 设置y轴的label;
    # plt.xlim(-1,3)      #可以自己设置x轴的坐标的范围哦;
    # plt.ylim(-1.5,1.5)   #同上;
    plt.title('About as simple as it gets, folks')
    plt.grid(True)  # 显示网格;

    plt.show()  # 显示出figure;


def fig_7():
    fig = plt.figure(1)
    ax1 = plt.subplot(111)
    ax2 = ax1.twinx()
    ax1.plot(np.arange(1, 5), 'g--')
    ax1.set_ylabel('ax1', color='r')
    ax2.plot(np.arange(7, 10), 'r-')
    ax2.set_ylabel('ax2', color='g')
    plt.show()

def fig_8():
    x1 = np.linspace(0.0, 5.0)  # 生成一个一维的array,linspace(起始点,结束点,点数(默认为50))
    x2 = np.linspace(0.0, 2.0)

    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    plt.subplot(2, 2, 1)  # 表示在subplot为2*1的样式,并在第一个子图上画出;
    plt.plot(x1, y1, 'yo-')
    plt.title('A tale of 2 subplots')
    plt.ylabel('Damped oscillation')

    plt.subplot(2, 2, 2)  # 我们在第二个子图上加个空图哈,去理解它的图的排序(即注意第二个子图的位置
    #  为第一行第二列)是按行优先的,这个正好和matlab里相反哦;

    plt.subplot(2, 2, 4)
    plt.plot(x2, y2, 'r.-')
    plt.xlabel('time (s)')
    plt.ylabel('Undamped')

    plt.show()


fig_8()