word="ProgramING"
cou_upper=0
cou_lower=0
for i in range(len(word)):
    if ord(word[i])>=65 and ord(word[i])<=90:
        cou_upper+=1
    else:
        cou_lower+=1
print(f"count of upper case letters is :{cou_upper}")
print(f"count of lower case letters is :{cou_lower}")