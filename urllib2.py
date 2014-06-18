# -*- coding: utf-8 -*-
import urllib2

url = r'http://www.ansen.org/p/allposts.html'
html = urllib2.urlopen(url).read()
print html
