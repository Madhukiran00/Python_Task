# # #string
  

# # #upper
# # name="madhu"
# # print(name.upper())

# # #lower
# # print(name.lower)

# #strip
# name1="   madhu     "
# print(name1.strip())

# #lstrip
# print(name1.lstrip())


# #rstrip

# print(name1.rstrip())

# #replace

# string="my name is madhu"

# print(string.replace("m","M"))
# print(string.replace("name","NAME"))

# #Startswith
# name="Madhu"
# print(name.startswith("M"))


# #endswith
# print(name.endswith("n"))


# #find

# string="my name is madhu"
# print(string.find("is"))
# print(string.find("k")) #it returns -1

# #count

# print(string.lower().count("m"))

# #title
# print(string.title())


# #capitalize
# print(string.capitalize())


# #Task:
# #   vowels="aeiou"
# string1="hyderabad"
# string1=string1.lower() 
# vowels="aeiou"

# for i in range(len(string1)):
#     ch=string1[i]
#     if vowels.find(ch)!=-1:
#         print(ch)


# for i in string1:
#     if i in  vowels:
#         print(i)

# take a string both upp ,lowe
#cuunt of vowels and count of consonents

string5="my name is madhu"
# index =string5.find("m")
# new_char = "M"
# new_string = string5[:index] + new_char + string5[index + 1:]
# print(new_string)


index=string5.find("m")
st="M"
print(string5[:index]+st+string5[index+1:])
