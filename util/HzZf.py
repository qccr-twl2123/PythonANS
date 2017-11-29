# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import tushare as ts
from  datetime  import  *


url = 'http://www.19lou.com/thread/category/structure/search/result?fid=1638&m=10003&page=1'
r = requests.get(url)
r.encoding = 'gb2312'
soup = BeautifulSoup(r.text,"lxml")

title_list = soup.find_all("a",class_="img_thread")
for title in title_list:
    print title.string

