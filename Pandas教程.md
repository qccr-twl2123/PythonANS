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
# 排序
df.sort(columns='sort')
```

* 选择算法
```python
# 1.通过下标
df['open']
# 2.选择多行
df[1:3]
```

* 合并

* 时间序列

