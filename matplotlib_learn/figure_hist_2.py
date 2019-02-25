import numpy as np
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def fig_1():
    # example data
    mu = 100  # mean of distribution
    sigma = 15  # standard deviation of distribution
    x = mu + sigma * np.random.randn(10000)      #np.random.randn(n)函数的作用为生成n个标准的正态分布的数;

    num_bins = 50
    # the histogram of the data
    n, bins, patches = plt.hist(x, bins = num_bins, normed=1, color='b',edgecolor = 'k', alpha=0.5, histtype='bar')
    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma) # normpdf(x,mu,sigma)：返回参数为μ和σ的正态分布密度函数在x处的值
                                                                # （其中参数mu是μ，参数sigma是σ)
    plt.plot(bins, y, 'r--')
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)   #把画的图从左边0.15(整个为1)处开始, 要不把y轴的label显示不出来 ,可以设为0试试.
                                                     # 另外,其实不加也没事;
    plt.show()

def fig_save():
    songTi = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
    plt.figure()
    plt.xticks(fontproperties=songTi, fontsize=12)
    plt.yticks(fontproperties=songTi, fontsize=12)
    plt.xlabel('用户听歌数量（首）', fontproperties=songTi, fontsize=14)
    plt.ylabel('人数占比（%）', fontproperties=songTi, fontsize=14)
    # plt.legend(fontsize=12)

    # 去除图形顶部边界和右边界的刻度
    # plt.tick_params(top= 'off', right= 'off')
    # 显示图例
    #plt.legend()

    fig = plt.gcf()
    fig.set_size_inches(7.2, 4.2)
    fig.savefig('D:/apaper/pic/用户听歌数量2.png', dpi=100)
    plt.show()


fig_1()