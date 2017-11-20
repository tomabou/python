s = """a n_0_0 2
a n_0_1 2
a n_0_2 2
a n_0_3 0
a n_0_4 4
a n_1_0 2
a n_1_1 2
a n_1_2 0
a n_1_3 0
a n_1_4 4
a n_1_5 4
a n_2_0 0
a n_2_1 2
a n_2_2 0
a n_2_3 4
a n_2_4 4
a n_2_5 4
a n_2_6 0
a n_3_0 6
a n_3_1 0
a n_3_2 0
a n_3_3 0
a n_3_4 0
a n_3_5 0
a n_3_6 0
a n_3_7 1
a n_4_0 6
a n_4_1 0
a n_4_2 5
a n_4_3 5
a n_4_4 5
a n_4_5 0
a n_4_6 1
a n_4_7 1
a n_4_8 1
a n_5_0 0
a n_5_1 5
a n_5_2 5
a n_5_3 5
a n_5_4 0
a n_5_5 0
a n_5_6 1
a n_5_7 1
a n_6_0 0
a n_6_1 0
a n_6_2 0
a n_6_3 0
a n_6_4 3
a n_6_5 0
a n_6_6 0
a n_7_0 6
a n_7_1 6
a n_7_2 0
a n_7_3 3
a n_7_4 3
a n_7_5 3
a n_8_0 6
a n_8_1 6
a n_8_2 0
a n_8_3 3
a n_8_4 3"""

ss = s.split('\n')
for s in ss:
    n = int(s[-5])
    if s[-3]=='0':
        print ''
        for i in range(abs(n-4)):
            print '',
    ans = int(s[-1])
    print ans,
    