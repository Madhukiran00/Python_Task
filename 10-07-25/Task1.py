l=[[5,9,6,3]]
target=9
for j in range(len(l)):
    for i in range(len(l[j])):
        if l[j][i]==target:
            if len(l)-1==0:
                print([i])
            else:
                print([j,i])