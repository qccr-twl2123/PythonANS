#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import tushare as ts

df = ts.profit_data(top=60)
df.sort('shares',ascending=False)

print  df