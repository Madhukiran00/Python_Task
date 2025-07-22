from django.urls import path
from . import views

urlpatterns=[
    path("mydetails/",view=views.mydetails)
]