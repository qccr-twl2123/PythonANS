#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
import traceback
def draw_test():
    try:

        plt.figure(1,figsize=(10, 4))  # 创建图表 1
        plt.figure(2,figsize=(20, 4))  # 创建图表 2 并且此时默认的对象是当前图表 2

        ax1 = plt.subplot(1,2,1)  # 在图表 2 中创建子图 1
        ax2 = plt.subplot(1,2,2)  # 在图表 2 中创建子图 2

        x = np.linspace(0, 3, 100)

        for i in xrange(5):
            plt.figure(1)                   # 切换到图表1
            plt.plot(x, np.exp(i * x / 3), label="line"+str(i+1))  # 第一次会在图表1中创建子图1，并且是当前的默认子图

            plt.sca(ax1) # 切换到图表 2 的子图 1当中
            plt.plot(x, np.sin(i * x), label="line"+str(i+1))

            plt.sca(ax2) # 切换到图表 2 的子图 2当中
            plt.plot(x, np.cos(i * x), label="line"+str(i+1))

        # 切换到图表1的 子图1 进行设置， 图表1只有1个子图，可以默认获得。不用保存。
        plt.figure(1)
        plt.title("Figure1")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.legend(loc=2)

        # 切换到图表 2 的子图 1当中
        plt.sca(ax1)
        plt.title("Figure2 Ax1")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.legend(loc=3)

        # 切换到图表 2 的子图 2当中
        plt.sca(ax2)
        plt.title("Figure2 Ax2")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.legend(loc=3)

        # 显示所有图表
        plt.show()
    except Exception,e:
        print traceback.print_exc()


draw_test()