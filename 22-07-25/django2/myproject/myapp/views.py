from django.http import HttpResponse;
from django.shortcuts import render;
from django.views.decorators.csrf import csrf_exempt;
import json
# Create your views here.



# def sample(req):


#     name=req.POST.get("name")
#     age=req.POST.get("age")
#     print(req.session)
#     return HttpResponse("makndsknfkdnsn")

# name=""
# @csrf_exempt
# def sample(req):
    
#     data=json.loads(req.body)
#     name=data["name"]
#     # print(data["name"])
#     return HttpResponse("django Project")
# print(name)



# name=""
# @csrf_exempt
# def sample(req):
    
#     data=req.POST.get("name")
#     print(data)
#     return HttpResponse("django Project")
# print(name)



name="hello"
@csrf_exempt
def sample(req):
    global name
    name=req.POST.get("name")
    age=req.POST.get("age")
    return HttpResponse("makndsknfkdnsn")
print("askfsdfkdshfkgds")
print(name)
@csrf_exempt
def show_name(req):
    return HttpResponse(f"{name}")
 



