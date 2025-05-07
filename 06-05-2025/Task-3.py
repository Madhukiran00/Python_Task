import math 
n=7
flag=True
for i in range(n,0,-1):
    res=""
    for j in range(1,3):
        if i==math.ceil(n/2) and flag==True:
                res+="* "*n
                flag=False
                break
        else:
            res+="*"+" "
    print(res)