#!/usr/bin/python
#coding: utf-8

import  tushare as ts
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'key1':['a','a','b','b','a'],
                'key2':['one','two','one','two','one'],
                'data1':np.random.randn(5),
                'data2':np.random.randn(5)})
print df
# 按key1进行分组
print df.groupby(df['key1']).mean()
# 先按key1进行分组,再按key2进行分组
print df.groupby([df['key1'], df['key2']]).mean()
# 分组计算,传入自定义函数, key1进行分组,对data1,data2进行max-min差值计算
print df.groupby('key1')['data1','data2'].agg(lambda arr:arr.max()-arr.min())





