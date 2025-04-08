#loops

# for ==> It is used when the iteration are finite
# while  ==> it is used when the iteration are not known
'''
for i in range(51):
    print(f"{i} Python is great")


limit=int(input("Enter the limit"))
for i in range(1,limit+1,1):
    if i%2==0:
        print(i)
        
    
for i in range(100,0,-1):
      print(i)   
    
    
for i in range(1,6,1):
    for j in range(1,21,1):
        print(f"{i}X{j}={i*j}\n")
        

for i in range(14,20,1):
    for j in range(1,11,1):
        print(f"{i}X{j}={i*j}\n"  

num=int(input("Enter no"))

for i in range(1,num+1):
'''

#task to 1-5
#1*2
#1*4
#1*6

fact=0
num=int(input("Enter the number\n"))
for i in range(1,num+1,1):
    if num%i==0:
        fact=fact+1
print(f"No of factors for {num} is {fact}")



'''
for i in range(1,6,1):
    for j in range(1,11,1):
        if j%2==0: 
            print(f"{i}X{j}={i*j}\n")
            '''