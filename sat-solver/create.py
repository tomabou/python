size = 3
target = [1,1,1,1,1,2]
l = len(target)
s = "; sp-1 problme\n"

def is_member(p,q):
    return (0<=p<=size*2-2)and(0<=q<size*2-1)and(-size<p-q<size)
for i in range(2*size+1):
    for j in range(2*size+1):
        if is_member(i,j):
            s+= "(int n_{}_{} 0 {})\n".format(i,j,l)

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