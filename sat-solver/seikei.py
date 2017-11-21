n = 3
s = input()
print(s)
while True:
    s = input()
    if len(s)==1:
        break
    else:
        x = int(s[4])
        y = int(s[6])
        ans = int(s[8])
        if (y==0) or (x-y ==n-1):
            for i in range(abs(x-n+1)):
                print(" ",end='')
        print("{} ".format(ans),end='')
        if (y==n*2-2) or (y-x == n-1 ):
            print("") 
        

        
