num=153 
temp=num
temp2=num
length=0
while num!=0: 
     num=num//10
     length+=1   
total_sum=0
while temp!=0:
     last=temp%10  
     total_sum= total_sum +  last**length  
     temp=temp//10
print(total_sum==temp2)