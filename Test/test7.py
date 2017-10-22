import numpy as np
import math
from scipy import stats
from numpy import array
from numpy.random import normal, randint
from numpy import array, cov, corrcoef

mu=np.mean((6.683,6.678,6.767,6.692,6.672,6.678))
std=np.std((6.683,6.678,6.767,6.692,6.672,6.678))
low = mu - stats.t.ppf(0.95,5) * std/ math.sqrt(6)
high = mu + stats.t.ppf(0.95,5) * std/ math.sqrt(6)
# print low
# print high



data1 = normal(0, 10, size=10)
data2 = randint(0, 10, size=10)

data = array([data1, data2])
# print data1,data2
# print data
print cov(data, bias=1)
