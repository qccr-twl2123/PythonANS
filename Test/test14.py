#!/usr/bin/python
#coding: utf-8

from scipy.stats import f_oneway
import  numpy as np
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import  pandas as pd
from scipy.stats import norm



order_id_file = open('11.text')
amount_file = open("12.text")
order_id_list =[]
amount_list = []
for line in order_id_file.readlines():
    order_id_list.append(str(line).replace("\n",""))

for line in amount_file.readlines():
    amount_list.append(float(line))

key_value = dict(zip(order_id_list,amount_list))
print key_value


