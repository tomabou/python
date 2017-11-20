"""test code"""
import re
import heapq

start_word = "ランゴ"
goal_word = "オドリ"
length_or_frequency = 3000


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


START = i
GOAL = i+1

def search_path():
    """do Dijkstra"""
    make_node(START, goal_word, 10, "ゴール")
    make_node(GOAL, start_word, 10, 'スタート')

    que = []
    heapq.heappush(que, (0, START))

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
                    ncost = cost + 1 + length_or_frequency/index_profile[nindex][1]
                    if not nindex in costs:
                        costs[nindex] = ncost
                        preindex[nindex] = v
                        heapq.heappush(que, (ncost, nindex))
                    elif ncost < costs[nindex]:
                        heapq.heappush(que, (ncost, nindex))
                        costs[nindex] = ncost
                        preindex[nindex] = v

    if GOAL not in costs:
        print("cannot reach")
    else:
        ind = GOAL
        while True:
            print(index_profile[ind])
            if ind==START:
                break
            ind = preindex[ind]
        
search_path()

#def search_path4():
#    """do Dijkstra"""
#    make_node(START, 'オヤカタ', 10, "ゴール")
#    make_node(GOAL, 'イキカタ', 10, 'スタート')

#    que = []
#    heapq.heappush(que, (0, START))

#    costs = dict()
#    preindex = dict()

#    while que != []:
#        (cost, v) = heapq.heappop(que)
#        (oyomi, ofreq, ka) = index_profile[v]

#        for nyomi in [oyomi[0]+oyomi[1]+c+oyomi[3] for c in KATAKANA] \
#            + [oyomi[0]+c+oyomi[2]+oyomi[3] for c in KATAKANA] \
#            + [oyomi[0]+oyomi[1]+oyomi[2]+c for c in KATAKANA] \
#            + [c+oyomi[1]+oyomi[2]+oyomi[3] for c in KATAKANA]:

#            if oyomi != nyomi and nyomi in yomi_to_index:
#                for nindex in yomi_to_index[nyomi]:
#                    ncost = cost + 1 + 5000/index_profile[nindex][1]
#                    if not nindex in costs:
#                        costs[nindex] = ncost
#                        preindex[nindex] = v
#                        heapq.heappush(que, (ncost, nindex))
#                    elif ncost < costs[nindex]:
#                        heapq.heappush(que, (ncost, nindex))
#                        costs[nindex] = ncost
#                        preindex[nindex] = v

#    if GOAL not in costs:
#        print("cannot reach")
#    else:
#        ind = GOAL
#        while True:
#            print(index_profile[ind])
#            if ind==START:
#                break
#            ind = preindex[ind]

#search_path4()