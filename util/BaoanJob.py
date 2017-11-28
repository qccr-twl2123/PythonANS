import requests
from lxml import html
url = 'http://www.51yhrc.com/search/hire_search.php?position=2441'
r = requests.get(url).content
sel = html.fromstring(r)

rs_center = sel.xpath('//div[@class="tab_title"]/text()')
for a in rs_center:
    print a