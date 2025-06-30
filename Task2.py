import random as r

a,b=map(int,input("Enter the range with space seperated:\n").split())
print("Game started!..❤️")
flag=False
rand_num=int(r.randint(a,b))

for i in range(3):
    num=int(input("Ges the number!...?\n"))
    if num == rand_num:
        print("🎉🎉..Congradulations 👍 \n You win the Game!🥳🥳 ")
        flag=True
    elif num>b or num<a:
        print("Num Out of range")
    if i<=2:
        if num<rand_num:
            print("forward..🧠")
        elif num>rand_num:
            print("backward..🧠")

if flag!=True:
    print("😔......Better Luck next Time.....😔")
    
    