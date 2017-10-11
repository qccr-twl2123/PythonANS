# my_drawing.py
# -*- coding:utf-8
import traceback
import random
from matplotlib import pyplot as plt
def draw_line( X, Y ):
    try:
        # 画框设置
        fig = plt.figure(figsize=(8, 5), dpi=80) # 创建图像
        axes = fig.add_subplot(111) # 创建一个1行1列的子图，axes是第1个图

        # 画点
        type1 = axes.plot(X, Y, label = "line1", c = 'red')

        # 加标题
        plt.title("Plot of X and Y")
        # 加坐标轴
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        # 加坐标轴范围
        plt.xlim(0.0, 7.0)
        plt.ylim(0.0, 30.0)

        # 加legend
        axes.legend(loc =2) # 设置legend位置

        # 显示
        plt.show()

    except Exception,e:
        print traceback.print_exc()

if __name__ == '__main__':
    draw_line([1,2,3,4,5],[1,4,9,16,25])