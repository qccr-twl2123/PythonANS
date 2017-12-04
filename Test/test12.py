#!/usr/bin/python
#coding: utf-8

from scipy.stats import f_oneway
import  numpy as np
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import  pandas as pd
from scipy.stats import norm

a = [87,86,76,56,78,98,77,66,75,67]   #群体1成绩
b = [87,85,99,85,79,81,82,78,85,91]  #群体2成绩
c = [89,91,96,87,89,90,89,96,96,93]  #群体3成绩
f,p = f_oneway(a,b,c)
print f
print p


key1 = ["a","a","a","a","a","a","a","a","a","a"]
key2 = ["b","b","b","b","b","b","b","b","b","b"]
key3 = ["c","c","c","c","c","c","c","c","c","c"]

dict1 = zip(a,key1)
dict2 = zip(b,key2)
dict3 = zip(c,key3)

df = pd.DataFrame(dict1+dict2+dict3,columns=["group","score"])

formula = 'group~C(score)'
model = ols(formula,df).fit()
results = anova_lm(model)
print results



