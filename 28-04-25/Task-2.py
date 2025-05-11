import copy

l1=[[1,2],[3,4]]
l2=[[1,2],[3,4]]

# print(id(l1),id(l2))

# l2=l1.copy()
# print(id(l1),id(l2))

l2=copy.deepcopy(l1)
print(id(l1[0]),id(l2[0]))

