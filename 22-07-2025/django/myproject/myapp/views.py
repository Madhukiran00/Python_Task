from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import products

# Create your views here.

def sample(req,id):
    for i in products.prod_list:
        if id==i["id"]:
            return JsonResponse(i)
        
   