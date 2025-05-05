k=1
n=5
for i in range(1,n+1):
    c=1
    for j in range(1,i+1):
        if (i>2 and   i<=n-1):
            if c==1 or  c==i:
                print(chr(96+k),end=" ")
                k+=1
                c+=1
            else:
                print(" ",end=" ")
                c+=1
                k+=1
        else:
            print(chr(96+k),end=" ")
            k+=1
        
    print("\n")
        