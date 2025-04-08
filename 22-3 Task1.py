list1=[{"name":"Madhu","age": 21,"citizen":"indian"},
       {"name":"kiran","age":17 ,"citizen":"indian"}]

for i in range(len(list1)):
    if list1[i]["age"]>18 and list1[i]["citizen"]=="indian":
        print(f"{list1[i]["name"]} is Eligible for vote")
    
    
    
       