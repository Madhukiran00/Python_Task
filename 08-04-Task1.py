num1=int(input("Enter the first no:"))
num2=int(input("Enter the secound no:"))
num3=int(input("Enter the secound no:"))

max_num=max(num1,num2,num3)
num=max_num
while True:
    if max_num%num1==0 and max_num%num2==0 and max_num%num3==0:
       print(f"lcm of {num1},{num2},{num3} is :",max_num)
       break
    else:
       max_num=max_num+num

       
         
