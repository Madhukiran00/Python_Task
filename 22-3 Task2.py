tup=(1,3,4,78,5,6,9,4,7,3,15,7)
new_list=[]

for i in range(len(tup)):
    cou=0
    cou=tup.count(tup[i])
    if cou==1:
        new_list.append(tup[i])
print(new_list)
