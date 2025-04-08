
str1="Python is a programming language that is used to build software"
True_count=0
False_count=0
for i in str1:
    if i==" " or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        True_count+=1
    else:
        False_count+=1
if False_count==0:
    print("valid String")
else:
    print("invalid String")
    