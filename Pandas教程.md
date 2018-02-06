### Pandas 教程
* 初始化
```python
# 1.创建DataFrame
import pandas as pd
import numpy as np
dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
#或
m_pd = pd.DataFrame(index=dates, columns=(['m2','m1','m0']))
m_pd['m0'] = None
m_pd['m1'] = None
m_pd['m2'] = None
# 2.从外部导入csv
df = pd.read_csv("test.csv",index_col="index")
```

* 常用方法
```python
# 查看前几条 head()
df.head()
# 查看后几天 tail()
df.tail()
# 基本描述
df.describe()
# 查看索引
df.index
# 查看列名
df.colunms
# 查看值
df.values
# 数据转置
df.T
# 按值排序
df.sort(columns='sort')
# 按index排序
df.sort_index(axis=1, ascending=False)
```

* select 选择
```python
# 1.通过下标
df['open']
# 2.选择多行
df[1:3]

# loc，基于列label，可选取特定行（根据行index）
# 使用标签获取横截面
df.loc[dates[0]]
# 使用标签选择多轴
df.loc[:,['A','B']]
# 显示标签切面,包含两个端点
df.loc['20130102':'20130104',['A','B']]
# 获取标量值
df.loc[dates[0],'A']

# iloc，基于行/列的position
print df.iloc[1:3, [1, 2]]
print df.iloc[1:3, 1: 3]

# at，根据指定行index及列label，快速定位DataFrame的元素；
df.at[dates[0],'A']

# iat，与at类似，不同的是根据position来定位的
print df.at[3, 'tip']
print df.iat[3, 1]

# ix，为loc与iloc的混合体，既支持label也支持position
print df.ix[1:3, [1, 2]]
print df.ix[1:3, ['total_bill', 'tip']]
```
* where 
```python
# df[df[colunm] boolean expr]
print df[df['sex'] == 'Female']
print df[df['total_bill'] > 20]

# or
print df.query('total_bill > 20')

# 在where子句中常常会搭配and, or, in, not关键词，Pandas中也有对应的实现：
# and
print df[(df['sex'] == 'Female') & (df['total_bill'] > 20)]
# or
print df[(df['sex'] == 'Female') | (df['total_bill'] > 20)]
# in
print df[df['total_bill'].isin([21.01, 23.68, 24.59])]
# not
print df[-(df['sex'] == 'Male')]
print df[-df['total_bill'].isin([21.01, 23.68, 24.59])]
# string function
print df = df[(-df['app'].isin(sys_app)) & (-df.app.str.contains('^微信\d+$'))]
```

* group 
```python
print df.groupby('sex').size()
print df.groupby('sex').count()
print df.groupby('sex')['tip'].count()

# 对于多合计函数
select sex, max(tip), sum(total_bill) as total
from tips_tb
group by sex;

# 实现在agg()中指定dict
print df.groupby('sex').agg({'tip': np.max, 'total_bill': np.sum})
# count(distinct **)
print df.groupby('tip').agg({'sex': pd.Series.nunique})

```

* 聚合计算
```python
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
```

* 时间序列

* 参考
```text
基本使用指南
http://python.jobbole.com/84416/
分组运算
https://my.oschina.net/lionets/blog/280332
sql一样的查询
https://www.cnblogs.com/en-heng/p/5630849.html
```

