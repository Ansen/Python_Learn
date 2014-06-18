import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.cnblogs.com')
soup = BeautifulSoup(r.text)
n = soup.find(id='headline_block').findAll('a')
n
for i in n:
    print i.text
