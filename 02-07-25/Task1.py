import os

#cwd() (current working directory)

print(os.getcwd())

#Output: /Users/madhukiran/Documents/GitHub/Python_Task

#--------------------------------------------------
#chdir() (change directory )

print("before:",os.getcwd())
os.chdir("/Users/madhukiran/Documents/GitHub")
print("after:",os.getcwd())

#Output: 
# before: /Users/madhukiran/Documents/GitHub/Python_Task
# after: /Users/madhukiran/Documents/GitHub

#--------------------------------------------------------

#mkdir()  (make directory)

os.chdir("/Users/madhukiran/Documents/GitHub/Python_Task/02-07-25")
os.mkdir("madhu")

# Output: it crates new folder

#---------------------------------------------

#listdir()
os.chdir("/Users/madhukiran/Documents/GitHub/Python_Task/02-07-25")
print(os.listdir())

#Output:
# ['madhu', 'Python', 'Task1.py']

#----------------------------------------------

#makedirs() For creating nexted folders

os.chdir("/Users/madhukiran/Documents/GitHub/Python_Task/02-07-25")
os.makedirs("Outer/inner")

# Output: it creates nexted folders

#--------------------------------------------------

#rmdir(). for delete the folder

os.chdir("/Users/madhukiran/Documents/GitHub/Python_Task/02-07-25")
os.rmdir("Outer")

#Output: it deletes outer folder

#--------------------------------------------

# rmdirs(). for deleting multiple folders

os.chdir("/Users/madhukiran/Documents/GitHub/Python_Task/02-07-25")
os.removedirs("madhu/inner")

#Output: id deletes both folders

#----------------------------------------------

#rename() for changing the folder name 

os.chdir("/Users/madhukiran/Documents/GitHub/Python_Task/02-07-25")
os.rename("madhu","Python")

# Output: rename the existing folder

#--------------------------------------------------

#path.exist()

print(os.path.exists("/Users/madhukiran/Documents/GitHub/Python_Task/02-07-25"))

# # Output: True

if not os.path.exists("/Users/madhukiran/Documents/GitHub/Python_Task/02-07-25"):
    
    os.mkdir("madhu")
else:
    print("Exist")

#Output:
# if this path is exists  retuen True
# if this path is not exists new folder created 
 
 #-----------------------------------------------------
 
#path.isdir()  to find weather the folder is exist or not

os.path.exists("/Users/madhukiran/Documents/GitHub/Python_Task/02-07-25")
print(os.path.isdir("python"))

#Output: False
#-------------------------------------------------------
# cpu_count() 
print(os.cpu_count())
# Output: 8
