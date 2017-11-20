"""test code"""
import re

PATTERN = re.compile("普通名詞")
FILE = open('BCCWJ_frequencylist_suw_ver1_0.tsv', 'r', errors='replace', encoding='utf-8')

i = 0
for line in FILE:
    l = line.split('\t')
    mOB = PATTERN.search(l[3])
    if mOB:
        if len(l[1]) == 4:
            i = i+1

print(i)