size = 3
target = [1,2]
l = len(target)
s = "; sp-1 problme\n"

def is_member(p,q):
    return (0<=p<=size*2-2)and(0<=q<size*2-1)and(-size<p-q<size)
for i in range(2*size+1):
    for j in range(2*size+1):
        if is_member(i,j):
            s+= "(int n_{}_{} 0 {})\n".format(i,j,l)

def nexts(p):
    a = p[0]
    b = p[1]
    return [(a-1,b-1),(a-1,b),(a,b-1),(a+1,b),(a+1,b+1),(a,b+1)]


def groups(n):
    if n==1:
        return [[(0,0)]]
    else:
        pre = groups(n-1)
        ans = set()
        for g in pre:
            for p in g:
                for new in nexts(p):
                    l = list(g)
                    if new not in l:
                        l.append(new)
                        l.sort()
                        mx = 0
                        my = 0
                        for p in l:
                            mx = min(mx,p[0])
                            my = min(my,p[1])
                        nl = [(p[0]-mx,p[1]-my) for p in l]
                        ans.add(tuple(nl))
        return list(ans)

for g in groups(3):
    print(g)

def group_comdition(x,y,group,index):
    for pos in group:
        if not is_member(x+pos[0],y+pos[1]):
            return False
    cnd = "  (and\n"
    bd = [[False for i in range(size*2+1)] for j in range(size*2+1)]    
    for pos in group:
        bd[x+pos[0]][y+pos[1]] = True
    for i in range(size*2-1):
        for j in range(size*2-1):
            if is_member(i,j):
                if bd[i][j]:
                    cnd += "    ( = n_{}_{} {})\n".format(x+pos[0],y+pos[1],index)
                else:
                    cnd += "    (!= n_{}_{} {})\n".format(x+pos[0],y+pos[1],index)
    cnd += "  )\n"
    return cnd

s += "( or\n"
for index in range(len(target)):
    gs = groups(target[index])
    for g in gs:
        for i in range(2*size+1):
            for j in range(2*size +1):
                cnd = group_comdition(i,j,g,index+1)
                if False == cnd:
                    continue
                else:
                    s += cnd
s+=")\n"

vals = ""
for i in range(2*size+1):
    for j in range(2*size+1):
        if is_member(i,j):
            vals+= "n_{}_{} ".format(i,j)

for i in range(len(target)):
    s+="(count {} ({}) eq {})\n".format(i+1 , vals, target[i])
    
def condition(a,b,p,q):
    return "(or (= n_{}_{} 0) (= n_{}_{} 0) (= n_{}_{} n_{}_{}))\n".format(a,b,p,q,a,b,p,q)

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
f = open('text.txt', 'w') 

f.write(s) 
f.close() 