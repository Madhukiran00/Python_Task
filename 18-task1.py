n=int(input("Enter the number\n"))
list1=[1,2,3,4,5,5,4,3,2]
count=0
for i in range(len(list1)):
    if list1[i]==n:
        count=count+1
print(f"The {n} number is repeated {count} times ")