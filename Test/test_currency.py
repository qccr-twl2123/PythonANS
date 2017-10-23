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
    print df
    dates = pd.to_datetime(list(df.columns)[1:-1],format="%Y-%m-%d")
    print  dates
    print df.T[0]

    # dates = df.index[1:-1]
    # x = pd.to_datetime(dates,format="%Y-%m")
    # print x



if __name__=="__main__":
     draw_line(pd.read_csv("2017-china-currency-provider.csv"))