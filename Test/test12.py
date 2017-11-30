#!/usr/bin/python
#coding: utf-8

from scipy.stats import f_oneway
import  numpy as np
from scipy import stats

a = [87,86,76,56,78,98,77,66,75,67]   #群体1成绩
b = [87,85,99,85,79,81,82,78,85,91]  #群体2成绩
c = [89,91,96,87,89,90,89,96,96,93]  #群体3成绩
f,p = f_oneway(a,b,c)
print f
print p
x = a+b+c
print stats.t.interval(0.95,len(x)-1,np.mean(x),stats.sem(x))

