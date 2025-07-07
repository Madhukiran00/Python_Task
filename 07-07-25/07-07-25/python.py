import requests
import json

# GET => USED TO RETRIVE DATA.
response=requests.get("https://fakestoreapi.com/products")
print(response.status_code)
print(response.json())
for i in response.json():
    print(i["title"])

response=requests.get("http://localhost:3000/users")
print(response.json())

# POST => USED TO SEND DATA TO A SERVER.

data={"name":"kiran"}
data=json.dumps(data)
response=requests.post(url="http://localhost:3000/users",data=data)
print(response.status_code)

#PUT => USED TO REPLACE THE  DATA  

data={"name":"madhu"}
response=requests.patch(url="http://localhost:3000/users/1",json=data)
print(response.status_code)
print(response.json())
print(response.text)

#PATCH => USED TO UPDATE THE DATA 

data={"name":"madhu"}
response=requests.patch(url="http://localhost:3000/users/1",json=data)
print(response.status_code)
print(response.json())
print(response.text)

# DELETE => USED TO DELETE THE DATA .

response=requests.delete("http://localhost:3000/users/2")
print(response.status_code)




