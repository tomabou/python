from bs4 import BeautifulSoup
from urllib.request import urlopen
 
html = urlopen("http://jp.yamaha.com/products/audio-visual/av-amplifiers/cx-a5100__j/?mode=model")
soup = BeautifulSoup(html,"lxml")
print(soup.find("h1"))
for i in soup.findAll("span",{"class":"val"}):
    print(i)