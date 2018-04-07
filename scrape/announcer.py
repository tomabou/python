from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import sys
import pandas as pd

def getInfo(name):
    name = urllib.parse.quote_plus(name)
    url = "https://ja.wikipedia.org/wiki/"+name
    html = urlopen(url)
    soup = BeautifulSoup(html,"lxml")
    res = soup.find("table",class_="infobox")
    df = pd.read_html(str(res))
    df = df[0]
    data = df[df[0]=="生年月日"]
    birthday="nd"
    if len(data)==1:
        birthday= data[1].values[0]
    hasband = "nd"
    data = df[df[0]=="配偶者"]
    if len(data)==1:
        hasband=data[1].values[0]
    
    return (birthday,hasband)

def announcerNames():
    name = urllib.parse.quote_plus("日本のアナウンサー一覧")
    url = "https://ja.wikipedia.org/wiki/"+name
    html = urlopen(url)
    soup = BeautifulSoup(html,"lxml")
    print(soup)

    names = ["江藤愛"]
    return names

if __name__=="__main__":
    names = announcerNames()
    birthdays=[]
    hasbands=[]
    for name in names:
        b,h=getInfo(name)
        birthdays.append(b)
        hasbands.append(h)
    dic = {"birhday":birthdays, "hasband":hasbands, "name":names}
    df = pd.DataFrame.from_dict(dic)
    #print(df.to_csv())
