from django.urls import path
from . import views

urlpatterns=[
    path("sample/",view=views.sample),
    path("show/",view=views.show_name)
]


