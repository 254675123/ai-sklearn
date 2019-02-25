import matplotlib.pyplot as plt
import numpy as np

def img_1():
    img = plt.imread('lena.jpg')
    print(img.shape)
    #输出为：    （256，256， 3）

    print(img.dtype)
    #输出为：   dtype('uint8')
    plt.imshow(img)
    plt.colorbar()    # 显示颜色映射表；

    plt.show()


def img_2():
    img = plt.imread('lena.jpg')
    fig = plt.figure(1)
    ax1 = plt.subplot(221)
    ax2 = plt.subplot(222)
    ax3 = plt.subplot(223)
    plt.sca(ax1)
    plt.imshow(img[:, :, 0])
    # plt.axis('off')
    plt.colorbar()
    plt.sca(ax2)
    plt.imshow(img[:, :, 1])
    # plt.axis('off')
    plt.colorbar()
    plt.sca(ax3)
    plt.imshow(img[:, :, 2])
    # plt.axis('off')
    plt.colorbar()
    plt.show()

img_2()