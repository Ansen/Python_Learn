# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2
import codecs
import time
import json
import sys

# ���UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0
reload(sys)
sys.setdefaultencoding('utf-8')


def novelFilter(content):
    content = content.replace('<br />\n<br />', '')
    content = content.replace('<br />', '')
    content = content.replace('&nbsp;', '')
    content = content.replace('<dd id="contents">', '')
    content = content.replace('</dd>', '')
    return content


def novelFetch(url, title):
    novel = urllib2.urlopen(url)
    soup = BeautifulSoup(novel.read().decode('gbk', 'ignore'))
    contents = '\n' + title + '\n' + str(soup.find('dd', id='contents'))
    contents = novelFilter(contents)

    print title.decode("utf-8")
    return contents


def novelSelect(url, mark):
    link = urllib2.urlopen(url)
    soup = BeautifulSoup(link.read().decode('gbk', 'ignore'))
    body = soup.findAll('td')

    flag = False
    cont = ''
    href = ''
    title = ''

    for i in body:
        try:
            href = url + i.a['href']
            title = str(i.a.string)

            if flag and href:
                cont += novelFetch(href, title)

            if title.decode("utf-8") == mark:
                flag = True

        except:
            pass

    return {
        'contents': cont,
        'bookmark': title
    }


def novelManage(info=0):
    if info:
        f = codecs.open('novel.json', 'w')
        f.write(json.dumps(info, indent=2, ensure_ascii=False))
        f.close()
    else:
        f = codecs.open('novel.json', 'r')
        info = json.loads(f.read())
    return info


if __name__ == '__main__':
    novels = novelManage()
    hasUpdate = False

    for title in novels:
        novel = novelSelect(novels[title]['url'], novels[title]['bookmark'])

        cont = novel['contents']
        bookmark = novel['bookmark']

        if cont and bookmark:
            novels[title]['bookmark'] = bookmark

            timesamp = time.strftime("%Y%m%d%H%M", time.localtime())
            f = codecs.open(title + '_' + timesamp + '.txt', 'w', 'gbk') #ʹ��gbk��ʽ
            f.write(cont)
            f.close()

            hasUpdate = True

    if not hasUpdate:
        print 'С˵û�и��¡�'.decode('utf-8')
    else:
        novelManage(novels)

