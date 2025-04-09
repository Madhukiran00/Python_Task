# list=[3,6,7,9,3,4,6,2,1,5,3]
# unq=[]
# for i in range(len(list)):
#     if list[i] not in unq:
#         unq.append(list[i])
#     else:
#         unq.append("*")
# print(unq)
#---------------------------------------------------

list=[3,6,7,9,3,4,6,2,1,5,3]
unq=[]
str=[]
for i in range(len(list)):
    if list[i] not in unq:
        unq.append(list[i])
    else:
        str.append("*")
unq.extend(str)
print(unq)  



