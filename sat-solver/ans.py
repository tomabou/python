s = """a n_0_0	5
a n_0_1	5
a n_0_2	5
a n_0_3	5
a n_0_4	5
a n_1_0	5
a n_1_1	0
a n_1_2	0
a n_1_3	0
a n_1_4	0
a n_1_5	5
a n_2_0	5
a n_2_1	0
a n_2_2	4
a n_2_3	4
a n_2_4	4
a n_2_5	0
a n_2_6	0
a n_3_0	0
a n_3_1	0
a n_3_2	0
a n_3_3	0
a n_3_4	4
a n_3_5	0
a n_3_6	3
a n_3_7	3
a n_4_0	0
a n_4_1	1
a n_4_2	0
a n_4_3	0
a n_4_4	4
a n_4_5	0
a n_4_6	3
a n_4_7	0
a n_4_8	0
a n_5_1	0
a n_5_2	1
a n_5_3	1
a n_5_4	0
a n_5_5	4
a n_5_6	0
a n_5_7	3
a n_5_8	3
a n_6_2	1
a n_6_3	0
a n_6_4	0
a n_6_5	0
a n_6_6	0
a n_6_7	0
a n_6_8	3
a n_7_3	1
a n_7_4	0
a n_7_5	2
a n_7_6	2
a n_7_7	2
a n_7_8	0
a n_8_4	1
a n_8_5	0
a n_8_6	2
a n_8_7	2
a n_8_8	2"""

ss = s.split('\n')
for s in ss:
    n = int(s[-5])
    if s[-3]=='0' or (int(s[-5])-int(s[-3]))==4:
        print ''
        for i in range(abs(n-4)):
            print '',
    ans = int(s[-1])
    print ans,
