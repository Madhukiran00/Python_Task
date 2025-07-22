from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# def sum(req):
#     return JsonResponse({"msg":"Hello"})

@csrf_exempt
def post_view(req):
    # print(req.method)
    if req.method=="POST" or req.method=="PUT" or req.method=="DELETE" :
        return HttpResponse("Post View")

# def put_view(req):
#     if "PUT"==req.method:
#         return HttpResponse("Put View")
    