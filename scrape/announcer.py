from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import sys
import pandas as pd

print(sys.getdefaultencoding())

name = "江藤愛"
name = urllib.parse.quote_plus(name)
url = "https://ja.wikipedia.org/wiki/"+name
#url = "https://matome.naver.jp/odai/2138128445557718901"
html = urlopen(url)
soup = BeautifulSoup(html,"lxml")
print(soup)