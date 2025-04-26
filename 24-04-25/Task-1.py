l=[5,3,50,6,10,2,15,30,]
res1=map(lambda num :num%5==0,l)
res2=filter(lambda num:num%5==0,l)
print(list(res1))
print(list(res2))