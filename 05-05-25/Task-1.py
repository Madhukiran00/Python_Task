
import math
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==1 or row==5 or col==1 or col==5 or  (row==math.ceil(n/2) and col==math.ceil(n/2)):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()