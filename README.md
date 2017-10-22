### 统计学基础概念

### 导图概览

![输入图片说明](https://github.com/qccr-twl2123/PythonANS/blob/master/images/0-统计-导图概览.png "在这里输入图片标题")


### 描述性统计-表格和图形法
![输入图片说明](https://github.com/qccr-twl2123/PythonANS/blob/master/images/1-描述性统计： 「表格和图形法」.png "在这里输入图片标题")

```text
1.理解什么是定量分析,什么是定性分析?
2.数据的分布形态有哪几种表示方法?
3.学会单变量和双变量研判趋势?
```

### 描述性统计-表格和图形法
![输入图片说明](https://github.com/qccr-twl2123/PythonANS/blob/master/images/2-描述性统计：数值方法.png "在这里输入图片标题")
```text
1.分位数,中位数,众数的概念?
2.方差 and 标准差
3.分布形态:偏度,峰度的理解?
4.协方差和相关系数的理解? 
5.定性数据,定量数据的理解?
```

```text
1.分位数,中位数,众数,平均数的概念?
    分位数:分位数是将总体按大小顺序排列后,处于各等分位置的变量值。
         如果将全部数据分成相等的两部分,它就是中位数;如果分成四等分,就是四分位数 
    众位数:出现次数最多的哪个数字
    
    pandas:
    df.mean()#列计算平均值
    df.mean(1)#行计算平均值
    df.median(0 or 1) 值得算术中位数（50%分位数）
    
    
    NumPy计算均值与中位数
    from numpy import mean, median
    
    #计算均值
    mean(data)
    #计算中位数
    median(data)

    于定性数据来说，众数是出现次数最多的值，使用SciPy计算众数
    
    from scipy.stats import mode
    #计算众数
    mode(data)

2.方差 and 标准差
    样本方差: 样本中各数据与样本平均数的差的平方和的平均数
    样本标准差: 样本方差的算术平方根(更适合描述数据波动范围)
    
    代码(pandas):
    d1.var() #方差
    d1.std() #标准差

3.协方差和相关系数
    协方差:两个样本变化方向相同则为正,相反则为负
    相关系数: 协方差的补充,描述两个样本的相似程度
    
    
```

* 方差计算公式

![输入图片说明](https://github.com/qccr-twl2123/PythonANS/blob/master/images/方差.png "在这里输入图片标题")

* 标准差计算公式

![输入图片说明](https://github.com/qccr-twl2123/PythonANS/blob/master/images/标准差.png "在这里输入图片标题")





#### 参考博客
```text
1.平方根与算数平方根
http://res.tongyi.com/resources/old_article/student/882.html

2.pandas 教程
https://www.joinquant.com/post/1981?f=study&m=python

3.Python进行描述性统计
http://www.cnblogs.com/jasonfreak/p/5441512.html

```

