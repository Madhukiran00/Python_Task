# file=open("./File/madhu.txt","r")
# res=''
# for char in file.readlines():
#     res+=char[0]
# print(res)

import os
# if os.path.exists("madhu.txt"):
#     file=open("madhu.txt","r")
#     res=''
#     for char in file.readlines():
#         res+=char[0]
#     print(res)
    
print(os.getcwd())  # Check current working directory
print(os.path.exists("madhu.txt"))   
    

    