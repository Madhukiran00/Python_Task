import os

user_inp=input("Enter folder name:")

base_path="/Users/madhukiran/Documents/GitHub/Python_Task/"

if os.path.exists(base_path+user_inp):
    os.chdir("/Users/madhukiran/Documents/GitHub/Python_Task/"+user_inp)
    with open("sample.txt","w") as file:
        file.write("This is sample file")
else:
    os.mkdir(user_inp)
    os.chdir("/Users/madhukiran/Documents/GitHub/Python_Task/"+user_inp)
    with open("sample.txt","w") as file:
        file.write("This is sample file")
    
        