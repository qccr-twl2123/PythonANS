### 统计学基础概念

### 导图概览

![输入图片说明](https://github.com/qccr-twl2123/PythonANS/blob/master/images/0-统计-导图概览.png "在这里输入图片标题")





```text
1.方差 and 标准差
共同点:描述样本的离散程度,即波动性
不同点:描述一个波动范围时标准差比方差更方便

计算公式:
样本方差: 样本中各数据与样本平均数的差的平方和的平均数
样本标准差: 样本方差的算术平方根

代码(pandas):
d1.var() #方差
d1.std() #标准差

```

* 方差计算公式

![输入图片说明](https://github.com/qccr-twl2123/PythonANS/blob/master/images/方差.png "在这里输入图片标题")

* 标准差计算公式

![输入图片说明](https://github.com/qccr-twl2123/PythonANS/blob/master/images/标准差.png "在这里输入图片标题")


### 连续随机变量研究范畴
```text

from scipy import stats
from scipy.stats import norm

rvs: Random Variates
pdf: Probability Density Function
cdf: Cumulative Distribution Function
sf: Survival Function (1-CDF)
ppf: Percent Point Function (Inverse of CDF)
isf: Inverse Survival Function (Inverse of SF)
stats: Return mean, variance, (Fisher’s) skew, or (Fisher’s) kurtosis
moment: non-central moments of the distribution

rvs:随机变量
pdf：概率密度函。
cdf：累计分布函数
sf：残存函数（1-CDF）
ppf：分位点函数（CDF的逆）
isf：逆残存函数（sf的逆）
stats:返回均值，方差，（费舍尔）偏态，（费舍尔）峰度。
moment:分布的非中心矩。





```


### 推断统计
* 置信区间,置信水平
```text
置信区间是我们所计算出的变量存在的范围
置信水平是我们对于这个数值存在于我们计算出的这个范围的可信程度。

举例来讲，有百分之九十五的把握，真正的数值在我们所计算出的范围里。
在这里，百分之九十五九十置信水平，而我们计算出的范围，就是置信区间。


```


#### 参考博客
```text
1.平方根与算数平方根
http://res.tongyi.com/resources/old_article/student/882.html

2.pandas 教程
https://www.joinquant.com/post/1981?f=study&m=python

```

