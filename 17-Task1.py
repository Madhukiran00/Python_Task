n=72
pnf=True
cou2=0
while pnf:
    cou1=0 
    n=n+1
    for i in range(1,n+1,1):
        if n%i==0: 
            cou1=cou1+1
            
    if cou1==2:
        cou2=cou2+1
        if cou2==2:
            pnf=False 
            print(n," is the next 2nd  prime number")
        

