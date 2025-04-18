Range=500
count=0
a,b=0,1 
for i in range(1,Range+1):
    a,b=b,a+b
    if a<=Range:
        count+=1
    else:
        break
print(count)

    
    
    