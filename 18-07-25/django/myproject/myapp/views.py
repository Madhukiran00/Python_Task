from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def mydetails(request):
    return JsonResponse({"NAME":"Madhu","MOB":"8317542543","EMAIL":"pillimadhukiran00@gmail.com"})
    