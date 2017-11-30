# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import tushare as ts
from  datetime  import  *

class HzZf(object):
    def __init__(self,url):
       self._url = url

    def get_content(self):
        html = requests.get(self._url)
        html.encoding = "gb2312"
        return html.text

    def get_list_content(self):
        soup = BeautifulSoup(self.get_content(),"lxml")
        item_list = soup.find_all("a",class_="img_thread")
        url_list = []
        for title in item_list:
            url_list.append("http:" + title["href"])

        return url_list

    def get_detail_content(self):
        for detail_url in self.get_list_content():
            html = requests.get(detail_url)
            html.encoding = "gb2312"
            soup = BeautifulSoup(html.text,"lxml")
            title = soup.find_all("span",attrs={"itemprop":"http://purl.org/dc/terms/title"})
            print title


if __name__ == '__main__':
    url = 'http://www.19lou.com/thread/category/structure/search/result?fid=1638&m=10003&page=2'
    zf = HzZf(url)
    zf.get_detail_content()



