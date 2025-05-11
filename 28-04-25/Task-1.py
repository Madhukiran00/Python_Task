string="aabbbc"  
temp=string[0]
count=0
res=""
for i in range(len(string)):
    if string[i]==temp:
        count+=1
    else:
        res+=temp+str(count)
        temp=string[i]
        count=1
res+=temp+str(count)
print(res)      




    