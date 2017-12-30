size = 5
target = [6,6,6,6,6,6]
filename = "sp1.txt"
l = len(target)
s = "; sp-1 problme\n"
zerolist = [(0,2),(1,0),(1,4),(2,2),(3,2),(3,6),(4,4),(5,2),(5,5),(5,7),(6,4),(8,7)]

def is_member(p,q):
    return (0<=p<=size*2-2)and(0<=q<size*2-1)and(-size<p-q<size)
for i in range(2*size+1):
    for j in range(2*size+1):
        if is_member(i,j):
            if (i,j) in zerolist:
                s+= "(int n_{}_{} 0 )\n".format(i,j)
            else:
                s+= "(int n_{}_{} 0 {})\n".format(i,j,l)
for i in range(2*size+1):
    for j in range(2*size+1):
        if is_member(i,j):
                s+= "(int c_{}_{} 0 )\n".format(i,j)
            else:
                s+= "(int c_{}_{} 0 {})\n".format(i,j,market(target))

def nexts(p):
    a = p[0]
    b = p[1]
    return [(a-1,b-1),(a-1,b),(a,b-1),(a+1,b),(a+1,b+1),(a,b+1)]

vals = ""
for i in range(2*size+1):
    for j in range(2*size+1):
        if is_member(i,j):
            vals+= "n_{}_{} ".format(i,j)

for i in range(len(target)):
    s+="(count {} ({}) eq {})\n".format(i+1 , vals, target[i])
    
def condition(a,b,p,q):
    ans = ""
    ans+="(or" 
    ans+= "(and (= n_{}_{} 0)(= c_{}_{} 0))".format(a,b,a,b)
    ans+= "(and (= n_{}_{} 0)(= c_{}_{} 0))".format(p,q,p,q)
    ans+= "(and"
    ans+= "  (= n_{}_{} n_{}_{})".format(a,b,p,q)
    ans+= "  "

s+="\n"
for i in range(2*size+1):
    for j in range(2*size+1):
        if is_member(i,j)and is_member(i,j+1):
            s+=condition(i,j,i,j+1)
s+="\n"

for i in range(2*size+1):
    for j in range(2*size+1):
        if is_member(i,j)and is_member(i+1,j):
            s+=condition(i,j,i+1,j)
s+="\n"

for i in range(2*size+1):
    for j in range(2*size+1):
        if is_member(i,j)and is_member(i+1,j+1):
            s+=condition(i,j,i+1,j+1)
s+=";END\n"

f = open(filename, 'w') 

f.write(s) 
f.close() 
