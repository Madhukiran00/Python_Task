
#GLobal 
x = 10
def change():
    global x
    x = 20
change()
print(x)  

#Local
def change():
    x = 20
    print(x)
change()

#enclosed

def outer():
    x = 20
    def inner():
        print(x)
    inner()
outer()

#built-in
def change():
    x = 20
    print(x)
change()


