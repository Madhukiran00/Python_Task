import random as r

digits=int(input("Enter the num of digits:\n"))
otp=""

for i in range(digits):
    otp+=str(r.randint(1,9))

print(otp)

 