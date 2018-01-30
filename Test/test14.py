#!/usr/bin/python
#coding: utf-8

from scipy.stats import f_oneway
import  numpy as np
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import  pandas as pd
from scipy.stats import norm
import tushare as ts

df = ts.get_stock_basics("600231")

print df




