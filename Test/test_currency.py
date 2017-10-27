#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def draw_line(china_currency):
    df = china_currency
    dates =pd.to_datetime(df.T.index,format="%Y-%m-%d")
    print dates
    m2 = df.T["M2"].values
    m1 = df.T["M1"].values
    plt.xticks(dates,rotation=45)
    plt.plot(m2,c="r")
    plt.plot(m1,c="g")

    plt.show()



if __name__=="__main__":
     draw_line(pd.read_csv("2017-china-currency-provider.csv",index_col="Item"))