set1={1,2,3,4,5,55,66}
set2={4,5,6,7,55,66}
set3={11,34,5,78,90}
set4=set()
#add
set1.add(5)
print(f" add :{set1}")

#remove  -->
set1.remove(5)
print(f"remove : {set1}")

#discard
set2.discard(7)
print(f"discard: {set2}")

#pop --->it  del first no of set 
set2.pop()
print(f"pop: {set2}")

#clear -->remove all elements from the set 
set3.clear()
print(f"clear: {set3}")

#union
print(f"union : {set1.union(set2)}")


#intersection -->return common to both sets

print(f"intersection: {set1.intersection(set2)}")

#difference  -->

print(f"difference: {set1.difference(set2)}")

#symmetric_difference

print(f"symmetric_difference: {set1.symmetric_difference(set2)}")




