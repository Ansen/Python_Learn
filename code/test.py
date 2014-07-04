#!/usr/bin/python
#coding:utf-8
#���ߣ�Byron
#���ͣ�http://jiabin.tk

import urllib2
import re

#�������������
def qiubai(page):
    url = "http://www.qiushibaike.com/week/page/%s" % page
    re_qb = re.compile(r'detail.*?<a.*?>(.*?)<.*?title="(.*?)">\s*(.*?)\s*?<', re.DOTALL)
    html = urllib2.urlopen(url).read()
    my_qiubai = re_qb.findall(html)
    for i in range(20):
        for k in range(3):
            print my_qiubai[i][k]
        s = raw_input("�س�����")
        if s == "q":
            exit()
        print "-" * 40

#�������ѭ����
def for_qb():
    for page in range(int(p), 281):
        print "-" * 18 + "��" + str(page) + "ҳ" + "-" * 18
        qiubai(page)

#�ò��ִ����Ŀ��Ϊ����Ƶ��Ͻ��������ܵ�ʹ���򲻷������
def if_qb():
    global p
    p = raw_input("����Ҫ����ҳ��1~280:")
    if p == "q":
        exit()
    elif not p.isdigit() or p == "0":
        if_qb()
    else:
        for_qb()


print "-" * 40
print "�ܰ������а桪��Byron"
print "һ���ܰ����ƺ����Ӵ˽ڲ���·��"
print '����"q"�˳�����'
print "-" * 40

if_qb()