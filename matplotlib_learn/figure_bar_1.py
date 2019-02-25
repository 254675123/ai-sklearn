# coding=utf8
'''
matplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
绘制条形图。绘制带有矩形边界的条形图通过如下设置：
left, left + width, bottom, bottom + height
(left, right, bottom and top edges)
输入参数：
left：标量序列。表示条形图左边x坐标。
height：标量或者标量序列。条形图的高度。
width：标量或者数组，可选参数。条形图宽度默认为：0.8。
bottom：标量或者数组，可选参数。条形图y坐标，默认值为None。
color：标量或者数组，可选参数。条形图前景色。
edgecolor：标量或者数组，可选参数。条形图边界颜色。
linewidth：标量或者数组，可选参数。条形图边界宽度。
                    如果为None，使用默认linewidth；如果为0，不画边界。默认为None。
tick_label：字符串或者数组，可选参数。条形图的tick标记，默认为None。
xerr:标量或者数组，可选参数。如果不是None，将把生成的errorbars用在条形图上，默认为None。
yerr:标量或者数组，可选参数。如果不是None，将把生成的errorbars用在条形图上，默认为None。
ecolor：标量或者数组，可选参数。指定errorbars的颜色，默认为None。
capsize：标量，可选参数。确定errorbars上限的长度，默认为None，从errorbar.capsize rcParam获取到值。
error_kw：字典类型，可选参数。kwags参数被传给errorbar方法。
                ecolor和capsize可能在这被指定而不是作为一个单独的kwargs。

align：{'center','edge'},可选参数，默认：'center'。
            如果是'edge'，通过左边界(条形图垂直)和底边界(条形图水平)来使条形图对齐。
            如果是'center'，将left参数解释为条形图中心坐标。
            通过传递一个给width设置复数，来使条形图以右边界进行对齐。
orientation：{'vertical','horizontal'},可选参数。设置条形图方向。
log：布尔类型，可选参数。如果为true，设置轴到log scale。默认为False。
返回值：
bars：matplotlib.container.BarContainer。带有所有bar与errorbar的容器。
-------------------------------------------------------------------------------
matplotlib.pyplot.barh(bottom, width, height=0.8, left=None, hold=None, **kwargs)
创建一个水平条形图。创建一个带有矩形边界的水平条，设置如下：
left, left + width, bottom, bottom + height
(left, right, bottom and top edges)
输入参数：
bottom：标量或者数组。条形图的y坐标。
width：标量或者数组。条形图宽度。
height：标量序列，可选参数，默认值为：0.8。条形图的高度。
left：标量序列。条形图左边的X坐标
返回值：
matplotlib.patches.Rectangle实例。
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys

# 提供汉字支持
mpl.rcParams["font.family"] = "sans-serif"
mpl.rcParams["font.sans-serif"] = u'SimHei'


def Vbar():
    # 绘制垂直条形图
    rect = plt.bar((0, 1, 2), height=(40, 30, 50), width=0.35, align="center")
    # 显示汉字，前面加u，代表使用unicode
    # y轴标记
    plt.ylabel(u'人数')

    # x轴标记
    plt.xlabel(u'班级')

    # 设置x轴可读显示
    plt.xticks((0, 1, 2), (u'一年级', u'二年级', u'三年级'))

    # 显示柱状图信息
    plt.legend((rect,), (u"图例",))
    # 显示绘制图片
    plt.show()


def Hbar():
    # 绘制水平条形图
    rect = plt.barh((0, 1, 2), height=0.35, width=(40, 30, 50), align="center")
    # 显示汉字，前面加u，代表使用unicode
    # y轴标记
    plt.ylabel(u'类别')

    # x轴标记
    plt.xlabel(u'数量')

    # 设置x轴可读显示
    plt.yticks((0, 1, 2), (u'文学类', u'历史类', u'哲学类'))

    # 显示柱状图信息
    plt.legend((rect,), (u"图例",))
    # 显示绘制图片
    plt.show()


if __name__ == "__main__":
    """
    注意：input() 和 raw_input() 这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。
注意：python3 里 input() 默认接收到的是 str 类型。
在 Python3.x 中 raw_input( ) 和 input( ) 进行了整合，去除了 raw_input( )，仅保留了 input( ) 函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
    """
    while True:
        choice = input(u"输入你的选择(V,H):")
        if choice in ["v", "V"]:
            Vbar()
        elif choice in ["h", "H"]:
            Hbar()
        else:
            print("Exit...")
            sys.exit()

