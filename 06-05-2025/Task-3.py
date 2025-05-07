n=5
c=True
for i in range(n,0,-1):
    for j in range(1,3):
        if n%2!=0 and c==True:
            print("*"*5)
            c==False
        else:
           print("*",end=" ")
    print("\n")