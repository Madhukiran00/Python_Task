'''
list=[1,2,3,4,5,6,7]
print(list.pop(list[1]))
print(list)


#remove
list=[1,2,6,4,9,3,7]
list.sort(reverse=True)
print(list)

list=[1,2,6,4,9,3,7]
list.sort(reverse=False)
print(list)

list=[1,2,6,4,9,3,7]
print(min(list))
print(max(list))'''

#print(chr(65))
#print(ord("A"))

'''
num=[x**2 for x in range(1,3) if x%2==0]
print(num)

list=[11,22,66,99,17,121]
for i in range(len(list)):
    if list[i]%11!=0:
        print(list[i])

#Task 1:
list=[2,4,5,8,9,34,5]
if list[0]%2==0 and list[(len(list)-1)]%2==0:
    print(True)
else:
    print(False)
    
Tak 2:
num=[1,2,3,4,5,6,6,7,1,5,3,5]
def cn(ele):
    count=0
    for i in range(0,len(num)):
        if num[i]==ele:
            count=count+1
    print(count)

ele=int(input("Enter no"))
cn(ele)
    
#my_list=[1,2,"hello",[1,2],True]

num=[1,2,2,3,4,4,5]
unq_list=[]

for ind in range(len(num)):
    if num.count(num[ind])==1:
        unq_list.append(num[ind])
print(unq_list)

'''

l=[1,2,3,4,5,6]
new_list=[]

new_list=[x for x in l if x%2==0]
print(new_list)

