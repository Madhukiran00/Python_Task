num=[1,2,3,4,5,6,7,8,9]
even_no=[]
odd_no=[]
for i in range(len(num)):
    if num[i]%2==0:
        even_no.append(i)
    else:
        odd_no.append(i)
odd_no.extend(even_no)
print(odd_no)

