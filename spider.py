# -*- coding: utf-8 -*-
'''
1、获取网址列表 get_url_list
2、网址检查，跟旧网址列表对比 check_url_list
3、若有新的网址则进入采集流程  get_content
4、过虑采集到的数据 content_filter
5、发布  content_post
'''
import urllib2
import re
url = r'http://www.ansen.org'
html = urllib2.urlopen(url).read()
start_tag ='<p'
finish_tag ='</p>'
reg = ''
content = re.compile(reg).findall(html)
filter_char = ['<div', '<a', 'head']

def deco(func,func2):
    content = re.compile(func).findall(func2)
    return content

@deco
def get_url_content():
    for i in filter_char:
        content = content.