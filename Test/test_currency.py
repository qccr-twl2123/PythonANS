#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def draw_line(china_currency):
    df = china_currency
    dates = pd.to_datetime(df.T.index)
    m0_1 = df.T["M0"].values
    m1_1 = df.T["M1"].values
    m2_1 = df.T["M2"].values
    m0 = [m0_1[i] for i in range(len(m0_1)) if np.isnan(m0_1[i]) == False]
    m1 = [m1_1[i] for i in range(len(m1_1)) if np.isnan(m1_1[i]) == False]
    m2 = [m2_1[i] for i in range(len(m2_1)) if np.isnan(m2_1[i]) == False]

    m_pd = pd.DataFrame(index=dates, columns=(['m0','m1','m2']))
    m_pd['m0'] = m0
    m_pd['m1'] = m1
    m_pd['m2'] = m2
    print m_pd.describe()

    plt.figure(figsize=(10, 7), dpi=80)
    plt.xticks(range(len(dates)),['2017-01-01', '2017-02-01', '2017-03-01', '2017-04-01',
                                  '2017-05-01', '2017-06-01', '2017-07-01', '2017-08-01',
                                  '2017-09-01', '2017-01-01', '2017-11-01', '2017-12-01'],rotation=45)
    # 曲线图
    # plt.plot(m2,c="r",label="M2",marker='o')
    # plt.plot(m1,c="g",label="M1",marker='*')
    # plt.plot(m0,c="b",label="M0")

    # 柱状图
    # plt.bar(range(9),m0,width=0.4,color="red")
    # plt.bar(range(9),m1,width=0.4,color="green")

    # 直方图
    plt.hist(m0,bins=12,range=9)

    plt.ylabel("供应量(万亿)")
    plt.xlabel("日期")
    # plt.ylim(np.array(m0).min(),np.array(m2).max())
    plt.grid(True,axis='y')

    plt.legend()
    plt.show()



if __name__=="__main__":
     draw_line(pd.read_csv("2017-china-currency-provider.csv",index_col="Item"))