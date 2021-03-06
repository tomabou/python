from PIL import Image
import sys
import random

def make_image(rule,mode = "simple",p=0.5):
    color1 = (0x66,0x99,0x99)
    color2 = (0xff,0x99,0x99)
    x = 1920
    y = 1080
    dotsize = 2
    filename = "rule"+str(rule)+"_"+str(x)+"x"+str(y)+"_"+str(dotsize)+"_"+mode+".png"
    img = Image.new('RGB',(x,y),color1) 

    rule_list = list()
    for i in range(8):
        rule_list.append(rule %2)
        rule = rule // 2

    print (rule_list)
    
    nx = x//dotsize + 1
    ny = y//dotsize + 1
    cell_map =[[0 for i in range(ny)] for j in range(nx+2) ] 
    if mode=="simple":
        cell_map[nx//(2)][0] = 1
    elif mode =="random":
        for i in range(nx):
            cell_map[i][0]=1 if random.random()<p else 0

    cell_map[nx][0]=cell_map[0][0]
    cell_map[nx+1][0]=cell_map[1][0]

    for j in range(ny-1):
        for i in range(nx):
            num = 4*cell_map[i][j] + 2* cell_map[i+1][j]+cell_map[i+2][j]
            cell_map[i+1][j+1] = rule_list[num]

        cell_map[0][j+1]=cell_map[nx][j+1]
        cell_map[nx+1][j+1]=cell_map[1][j+1]
        

    for i in range(x):
        for j in range(y):
            if cell_map[i//dotsize][j//dotsize]==1:
                img.putpixel((i,j),color2)
    
    img.save(filename)
    return img

if __name__ == "__main__":
    argv = sys.argv
    if len(argv)==1:
        rule = 30 
    else:
         rule = int(argv[1])
    if len(argv)<=2:
        mode = "simple"
    else:
        mode = argv[2]
    
    if len(argv)>3:
        p = float(argv[3])
    else:
        p = 0.5

    img = make_image(rule,mode,p)
    img.show()
