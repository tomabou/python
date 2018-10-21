from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import sys
import pandas as pd
import matplotlib.pyplot as plt
import time
import pickle

from matplotlib.font_manager import FontProperties
import matplotlib

font_path = '/home/tomabo/Downloads/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)


def get_data(datas, table_num, data_idx):
    data = datas[table_num]
    table = data.table
    df = pd.read_html(str(table))
    df = df[0]
    print(df.iloc[data_idx, 0])
    return df.iloc[data_idx, 2]


def get_name(datas, table_num, data_idx):
    data = datas[table_num]
    table = data.table
    df = pd.read_html(str(table))
    df = df[0]
    return df.iloc[data_idx, 0]


def getInfo(num, tds, page=18):
    url = "https://www.j-magazine.or.jp/user/printed/index/" + \
        str(num)+"/"+str(page)
    html = urlopen(url)
    time.sleep(1)
    soup = BeautifulSoup(html, "lxml")
    datas = soup.find_all(class_="MagDataTab")

    result = []
    for (t, d) in tds:
        result.append(get_data(datas, t, d))
    return result


def get_names(ptds, page=18):
    url = "https://www.j-magazine.or.jp/user/printed/index/" + \
        str(1)+"/"+str(page)
    html = urlopen(url)
    time.sleep(1)
    soup = BeautifulSoup(html, "lxml")
    datas = soup.find_all(class_="MagDataTab")

    result = []
    for (table_num, data_idx) in tds:
        data = datas[table_num]
        table = data.table
        df = pd.read_html(str(table))
        df = df[0]
        result.append(df.iloc[data_idx, 0])
    return result


def get_by_name(num, names, page):
    url = "https://www.j-magazine.or.jp/user/printed/index/" + \
        str(num)+"/"+str(page)
    html = urlopen(url)
    time.sleep(1)
    soup = BeautifulSoup(html, "lxml")
    datas = soup.find_all(class_="MagDataTab")

    result = []
    for name in names:
        result.append(_choose_by_name(datas, name))
    return result


def _choose_by_name(datas, name):
    for data in datas:
        table = data.table
        df = pd.read_html(str(table))
        df = df[0]
        for i in range(1, len(df.index)):
            n = df.iloc[i, 0]
            if name == n:
                return df.iloc[i, 2]


if __name__ == "__main__":
    ptds = [
        (19, ["an・an"]),
        (17, [(2, 1)]),
        (18, [(0, 1), (0, 2), (0, 3), (0, 4), (1, 1)])
    ]
    allres = []
    allname = []
    for (page, tds) in ptds:
        if page == 19:
            results = [[] for _ in range(len(tds))]
            for i in range(1, 41):
                res = get_by_name(i, tds, page=page)
                print(res)
                for j, result in enumerate(res):
                    results[j].append(int(result)/10000)
            names = tds
            print(results)
            print(names)
        else:
            results = [[] for _ in range(len(tds))]
            for i in range(1, 41):
                res = getInfo(i, tds, page=page)
                for j, result in enumerate(res):
                    results[j].append(int(result)/10000)
            names = get_names(tds, page=page)
            print(results)
            print(names)

        allres = allres+results
        allname = allname+names

    import datetime
    y = []
    for i in range(40):
        year = 2008+i//4
        m = i % 4 * 3+1
        y.append(datetime.date(year, m, 1))

    for (res, name) in zip(allres, allname):
        plt.plot(y, res, label=name)
    plt.title("ファッション誌の印刷部数", fontproperties=font_prop)
    plt.xlabel("発行日", fontproperties=font_prop)
    plt.ylabel("印刷部数(万)", fontproperties=font_prop)
    plt.legend()
    plt.show()
