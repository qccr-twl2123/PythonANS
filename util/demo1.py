# coding:utf-8
import requests

from lxml import html
url = 'https://movie.douban.com/chart'

r = requests.get(url).content
sel = html.fromstring(r)

# 提取h1标签
title = sel.xpath("//h1/text()")

# 提取链接
links = sel.xpath('//div[@class="pl2"]/a/@href')

# 上面返回的是所有符合条件的链接的列表，for循环来读取一下
for link in links:
    print link