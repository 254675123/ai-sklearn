import numpy as np
import matplotlib.pyplot as plt

def sca_1():
    x = [0,2,4,6,8,10]
    y = [0]*len(x)
    s = [20*4**n for n in range(len(x))]
    plt.scatter(x,y,s=s)
    plt.show()

def sca_2():
    x = [0, 2, 4, 6, 8, 10]
    y = [0] * len(x)
    s = [20 * 2 ** n for n in range(len(x))]
    plt.scatter(x, y, s=s)
    plt.show()


def sca_3():
    fig = plt.figure(figsize=(8, 6))
    # Generating a Gaussion dataset:
    # creating random vectors from the multivariate normal distribution
    # given mean and covariance
    mu_vec1 = np.array([0, 0])
    cov_mat1 = np.array([[1, 0], [0, 1]])

    #
    # np.random.multivariate_normal方法用于根据实际情况生成一个多元正态分布矩阵
    # multivariate_normal(mean, cov, size=None, check_valid=None, tol=None)
    # 其中mean和cov为必要的传参而size，check_valid以及tol为可选参数。
    X = np.random.multivariate_normal(mu_vec1, cov_mat1, 500)
    R = X ** 2
    R_sum = R.sum(axis=1)
    plt.scatter(X[:, 0], X[:, 1], color='green', marker='o',
                s=32. * R_sum, edgecolor='black', alpha=0.5)

    plt.show()

def sca_4():
    # Generating a Gaussion dTset:
    # Creating random vectors from the multivaritate normal distribution
    # givem mean and covariance

    mu_vecl = np.array([0, 0])
    cov_matl = np.array([[2, 0], [0, 2]])

    x1_samples = np.random.multivariate_normal(mu_vecl, cov_matl, 100)
    x2_samples = np.random.multivariate_normal(mu_vecl + 0.2, cov_matl + 0.2, 100)
    x3_samples = np.random.multivariate_normal(mu_vecl + 0.4, cov_matl + 0.4, 100)

    plt.figure(figsize=(8, 6))

    plt.scatter(x1_samples[:, 0], x1_samples[:, 1], marker='x',
                color='blue', alpha=0.7, label='x1 samples')
    plt.scatter(x2_samples[:, 0], x1_samples[:, 1], marker='o',
                color='green', alpha=0.7, label='x2 samples')
    plt.scatter(x3_samples[:, 0], x1_samples[:, 1], marker='^',
                color='red', alpha=0.7, label='x3 samples')
    plt.title('Basic scatter plot')
    plt.ylabel('variable X')
    plt.xlabel('Variable Y')
    plt.legend(loc='upper right')

    plt.show()

def sca_5():
    fig, ax = plt.subplots()
    # plot 可以画圆点（画圆点时，圆点的大小由markersize指定），也可以画直线；
    # scatter也可以画圆点，圆点的大小由s参数指定，这里的s=markersize ** 2
    # 也就是s = markersize * markersize
    # plot的参数，第一个参数为[x1, x2,...], 第二个参数为[y1, y2, ...]
    # 画图的时候[x1, y1]会组合成一个点
    ax.plot([0], [0], marker="o", markersize=10)
    ax.plot([0.07, 0.93], [0, 0], linewidth=10)
    ax.scatter([1], [0], s=100)

    ax.plot([0], [1], marker="o", markersize=22)
    ax.plot([0.14, 0.86], [1, 1], linewidth=22)
    ax.scatter([1], [1], s=22 ** 2)

    plt.show()

def sca_6():
    for dpi in [72, 100, 144]:
        fig, ax = plt.subplots(figsize=(1.5, 2), dpi=dpi)
        ax.set_title("fig.dpi={}".format(dpi))
        # 设置y轴，x轴的范围
        ax.set_ylim(-3, 3)
        ax.set_xlim(-2, 2)

        ax.scatter([0], [1], s=10 ** 2,
                   marker="s", linewidth=0, label="100 points^2")
        ax.scatter([1], [1], s=(10 * 72. / fig.dpi) ** 2,
                   marker="s", linewidth=0, label="100 pixels^2")

        ax.legend(loc=8, framealpha=1, fontsize=8)

        fig.savefig("fig{}.png".format(dpi), bbox_inches="tight")

    plt.show()


def sca_7():
    x1 = np.random.randn(20)
    x2 = np.random.randn(20)
    plt.figure(1)
    # you can specify the marker size two ways directly:
    plt.plot(x1, 'bo', markersize=20)  # blue circle with size 10
    plt.plot(x2, 'ro', ms=10, )  # ms is just an alias for markersize
    plt.show()

def sca_8():
    plt.scatter(2, 1, s=4000, c='r')
    plt.scatter(2, 1, s=1000, c='b')
    plt.scatter(2, 1, s=10, c='g')
    plt.show()

def sca_9():
    x_coords = [0.13, 0.22, 0.39, 0.59, 0.68, 0.74, 0.93]
    y_coords = [0.75, 0.34, 0.44, 0.52, 0.80, 0.25, 0.55]

    fig = plt.figure(figsize=(8, 5))

    plt.scatter(x_coords, y_coords, marker='s', s=50)
    for x, y in zip(x_coords, y_coords):
        plt.annotate('(%s,%s)' % (x, y), xy=(x, y), xytext=(0, -10), textcoords='offset points', ha='center', va='top')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.show()


def sca_10():
    # 2-category classfication with random 2D-sample data
    # from a multivariate normal distribution

    def decision_boundary(x_1):
        """Calculates the x_2 value for plotting the decision boundary."""
        return 4 - np.sqrt(-x_1 ** 2 + 4 * x_1 + 6 + np.log(16))

    # Generating a gaussion dataset:
    # creating random vectors from the multivariate normal distribution
    # given mean and covariance

    mu_vec1 = np.array([0, 0])
    cov_mat1 = np.array([[2, 0], [0, 2]])
    x1_samples = np.random.multivariate_normal(mu_vec1, cov_mat1, 100)
    mu_vec1 = mu_vec1.reshape(1, 2).T  # TO 1-COL VECTOR

    mu_vec2 = np.array([1, 2])
    cov_mat2 = np.array([[1, 0], [0, 1]])
    x2_samples = np.random.multivariate_normal(mu_vec2, cov_mat2, 100)
    mu_vec2 = mu_vec2.reshape(1, 2).T  # to 2-col vector

    # Main scatter plot and plot annotation

    f, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(x1_samples[:, 0], x1_samples[:, 1], marker='o', color='green', s=40)
    ax.scatter(x2_samples[:, 0], x2_samples[:, 1], marker='^', color='blue', s=40)
    plt.legend(['Class1 (w1)', 'Class2 (w2)'], loc='upper right')
    plt.title('Densities of 2 classes with 25 bivariate random patterns each')
    plt.ylabel('x2')
    plt.xlabel('x1')
    ftext = 'p(x|w1) -N(mu1=(0,0)^t, cov1 = I)\np.(x|w2) -N(mu2 = (1, 1)^t), cov2 =I'
    plt.figtext(.15, .8, ftext, fontsize=11, ha='left')

    # Adding decision boundary to plot

    x_1 = np.arange(-5, 5, 0.1)
    bound = decision_boundary(x_1)
    # r-- 的，r代表红色red，-- 代表虚线样式
    # lw=3，表示linewidth=3的简写
    plt.plot(x_1, bound, 'r--', lw=3)
    # numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    # 在指定的间隔内返回均匀间隔的数字，返回num均匀分布的样本，在[start, stop]；
    # 这个区间的端点可以任意的被排除在外。
    x_vec = np.linspace(*ax.get_xlim())
    x_1 = np.arange(0, 100, 0.05)

    plt.show()


sca_10()