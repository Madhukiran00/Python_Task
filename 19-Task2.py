#Task 2:
num=[1,2,3,4,5,6,6,7,1,5,3,5]
def cn(ele):
    count=0
    for i in range(0,len(num)):
        if num[i]==ele:
            count=count+1
    print(f"The {ele} no repeated in {count} times")

ele=int(input("Enter no\n"))
cn(ele)