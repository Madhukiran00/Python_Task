list1=[4,6,9,12,15,2,8]
min_no=min(list1)
max_no=max(list1)
mis_no=[]

for i in range(min_no,max_no,1):
    if i in list1:
        pass
    else:
        mis_no.append(i)
print(f"Missing no's is:{mis_no}")