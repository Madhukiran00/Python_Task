num=13759
while num!=0:
    last_num=num%10
    count=0
    for i in range(1,last_num+1,1):
        if last_num%i==0:  
            count=count+1
    if count==2:
        print(last_num)
    num=num//10
    
