size = 5
target = [6,6,6,7,7,7]
l = len(target)
s = "; sp-1 problme\n"

for i in range(size):
    for j in range(i+size):
        s+= "(int n_{}_{} 0 {})\n".format(i,j,l)

for i in range(size-1):
    for j in range(size*2 - 2-i):
        s+= "(int n_{}_{} 0 {})\n".format(i+size,j,l)

vals = ""
for i in range(size):
    for j in range(i+size):
        vals+= "n_{}_{} ".format(i,j)

for i in range(size-1):
    for j in range(size*2 - 2-i):
        vals+= "n_{}_{} ".format(i+size,j)

for i in range(len(target)):
    s+="(count {} ({}) eq {})\n".format(i+1 , vals, target[i])


def condition(a,b,p,q):
    return "(or (= n_{}_{} 0) (= n_{}_{} 0) (= n_{}_{} n_{}_{}))\n".format(a,b,p,q,a,b,p,q)

s+="\n"
for i in range(size):
    for j in range(i+size-1):
        s+=condition(i,j,i,j+1)
for i in range(size-1):
    for j in range(size*2 - 3-i):
        s+=condition(i+size,j,i+size,j+1)
s+="\n"
for i in range(size-1):
    for j in range(i+size):
        s+=condition(i,j,i+1,j)
for i in range(size-1):
    for j in range(size*2 - 2-i):
        s+=condition(i+size-1,j,i+size,j)
s+="\n"
for i in range(size-1):
    for j in range(i+size):
        s+=condition(i,j,i+1,j+1)
for i in range(size-1):
    for j in range(i+size):
        s+=condition(size*2-2-i,j,size*2-3-i,j+1)

s+=";END\n"
f = open('text.txt', 'w') 

f.write(s) 
f.close() 