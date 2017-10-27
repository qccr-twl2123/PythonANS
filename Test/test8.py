#!/usr/bin/python
# -*- coding: UTF-8 -*-

#文件操作

import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


data_xls = pd.read_excel('b.xlsx', 'Sheet1', index_col = 0)
df = data_xls.T
# print  df

file = open('demo.text')

key_list = []
values_list = []
for  line in  file.readlines():
    # key值生成
    char_list = line.split()[0].split("_")
    key =""
    for i in range(len(char_list)):
        if(i>0):
            key += char_list[i].capitalize()
        else:
            key=char_list[i]

    key_list.append(key)
    #value 值集合生成
    values_list.append(line.split()[1])



print key_list
print values_list

key_value = dict(zip(key_list,values_list))
print key_value




