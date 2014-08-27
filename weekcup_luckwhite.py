#coding=utf8

import  urllib2, re

def get_rankpage_url():
    url = 'http://www.taojingu.cn/news/?classid=329'
    response = urllib2.urlopen(url).read()
    rankpage = re.findall('href="/news/view.aspx[?]id=(.*?)"(.*?)</a>', response, re.S)
    rankpageid = []
    for i in range(0, 5):
        test = rankpage[i]
        rankpageid.append(test[0])
    return rankpageid

def get_whitelist(pageid):
    for i in pageid:
        url = 'http://www.taojingu.cn/news/view.aspx?id=' + i
        response = urllib2.urlopen(url).read()
        rank = re.findall('<tr class="row"><td class="cr1">(.*?)</td><td class="cr2">(.*?)</td><td class="cr3">', response, re.S)
        for i in range(57, len(rank), 10):
            userid = rank[i]
            print userid[1]

get_whitelist(get_rankpage_url())