#coding=utf8

import urllib2, re,datetime

url = 'http://www.taojingu.cn/news/?classid=329'
response = urllib2.urlopen(url).read()
#print response
rankpage = re.findall('href="/news/view.aspx[?]id=(.*?)"(.*?)</a>', response, re.S)
rankpageid = []
for i in range(0, 5):
    test = rankpage[i]
    rankpageid.append(test[0])

return rankpageid
    

