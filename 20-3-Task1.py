list=[2,5,7,15,6,1,45,86]
prime_list=[]
Non_prime_list=[]

for i in range(len(list)):
    cou=0
    for j in range(1,list[i]+1,1):
        if list[i]%j==0:
            cou=cou+1
    if cou==2:
        prime_list.append(list[i])
    else:
        Non_prime_list.append(list[i])
print("prime_list:",prime_list)
print("Non_prime_list:",Non_prime_list)
        