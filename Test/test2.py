#my_drawing.py
#-*- coding:utf-8
import traceback
import random
from matplotlib import pyplot as plt

def draw_scatter(X1, Y1, X2, Y2, X3, Y3):
    try:
        # 画框设置
        fig = plt.figure(figsize=(8, 5), dpi=80)  # 创建图像
        axes = fig.add_subplot(111)  # 创建一个1行1列的子图，axes是第1个图

        # 画点
        type1 = axes.scatter(X1, Y1, label = "Do not like", s=20, c='red')
        type2 = axes.scatter(X2, Y2, label = "Just so so",  s=40, c='green')
        type3 = axes.scatter(X3, Y3, label = "Very much",   s=50, c='blue')

        # 加标题
        plt.title("Scatter plot")
        # 加坐标轴
        plt.xlabel("Miles per year")
        plt.ylabel("Percentage it cost")
        # 加legend
        axes.legend(loc=2)

        # 显示
        plt.savefig("sandiantu.png")
        plt.show()


    except Exception, e:
        print traceback.print_exc()

if __name__ == '__main__':

    table1_x = []
    table1_y = []
    # generate the dataset
    for i in range(0,100):
        x = random.randint(1,100)
        y = random.randint(1,100)
        table1_x.append(x)
        table1_y.append(y)


    table2_x = []
    table2_y = []
    # generate the dataset
    for i in range(0, 100):
        x = random.randint(401, 500)
        y = random.randint(401, 500)
        table2_x.append(x)
        table2_y.append(y)


    table3_x = []
    table3_y = []
    # generate the dataset
    for i in range(0, 100):
        x = random.randint(900, 1000)
        y = random.randint(900, 1000)
        table3_x.append(x)
        table3_y.append(y)


    draw_scatter(table1_x, table1_y, table2_x, table2_y, table3_x, table3_y)