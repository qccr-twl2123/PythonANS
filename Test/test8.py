#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


data_xls = pd.read_excel('b.xlsx', 'Sheet1', index_col = 0)
df = data_xls.T
print  df

