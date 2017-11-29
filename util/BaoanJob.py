import requests
from lxml import html
url = 'http://www.19lou.com/thread/category/structure/search/result?m=10001&fid=1637&mf_1391=4'
html = requests.get(url)
html.encoding = "UTF-8"
html = html.content
print html
sel = html.fromstring(html)

table = sel.xpath('//form[@id="J_threadForm"]/text()')
print table
