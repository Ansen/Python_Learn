#coding=utf8
from contextlib import closing
import  urllib2, re

def re_rule(url,rule):
    with closing(urllib2.urlopen(url)) as response:
        content = re.findall(rule, response.read(), re.S)
        return content

def get_rankpage_url(rankpage):
        rankpageid = []
        for i in range(0, 5):
            test = rankpage[i]
            rankpageid.append(test[0])
        return rankpageid

def get_whitelist(pageid,rule):
    luckid = []
    for i in pageid:
        url = 'http://www.taojingu.cn/news/view.aspx?id=' + i
        rank = re_rule(url, rule)
        for i in range(57, len(rank), 10):
            userid = rank[i]
            luckid.append(userid[1])
    return luckid

newsurl = 'http://www.taojingu.cn/news/?classid=329'
newsrule = 'href="/news/view.aspx[?]id=(.*?)"(.*?)</a>'
pagerule = '<tr class="row"><td class="cr1">(.*?)</td><td class="cr2">(.*?)</td><td class="cr3">'
luckid = list(set(get_whitelist(get_rankpage_url(re_rule(newsurl, newsrule)), pagerule)))

for i in luckid:
    print i