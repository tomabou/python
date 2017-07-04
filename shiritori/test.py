"""test code"""
import re
import heapq


PATTERN = re.compile("普通名詞")
print("hello")
KATAKANA = [chr(i) for i in range(12449, 12532+1)]
FILE = open('BCCWJ_frequencylist_suw_ver1_0.tsv', 'r', errors='replace', encoding='utf-8')
index_profile = list()
yomi_to_index = dict() 

def make_node(index, yomi, frequency, kanji):
    """make node for Dijkstra"""
    index_profile.append((yomi, frequency, kanji))
    if not yomi in yomi_to_index:
        yomi_to_index[yomi] = [index]
    else:
        yomi_to_index[yomi].append(index)

i = 0
for line in FILE:
    l = line.split('\t')
    mOB = PATTERN.search(l[3])
    if mOB:
        if len(l[1]) == 3:
            make_node(i, l[1], float(l[6]), l[2])
            i = i+1


start = i 
goal = i+1 
make_node(start, 'ショウ', 10, "スタート")
make_node(goal, 'エグサ', 10, 'ゴール')

que = [] 
heapq.heappush(que, (0, start))

costs = dict()
preindex = dict()

while que != []:
    (cost, v) = heapq.heappop(que)
    (oyomi, ofreq, ka) = index_profile[v]

    for nyomi in [oyomi[0]+oyomi[1]+c for c in KATAKANA] \
        + [oyomi[0]+c+oyomi[2] for c in KATAKANA] \
        + [c+oyomi[1]+oyomi[2] for c in KATAKANA]:

        if oyomi != nyomi and nyomi in yomi_to_index:
            for nindex in yomi_to_index[nyomi]:
                ncost = cost + 1 + 500/index_profile[nindex][1]
                if not nindex in costs:
                    costs[nindex] = ncost
                    preindex[nindex] = v
                    heapq.heappush(que, (ncost, nindex))
                elif ncost < costs[nindex]:
                    heapq.heappush(que, (ncost, nindex))
                    costs[nindex] = ncost
                    preindex[nindex] = v
        
if goal not in costs:
    print("cannot reach")
else:
    ind = goal
    while True:
        print(index_profile[ind])
        if ind==start:
            break
        ind = preindex[ind]
    