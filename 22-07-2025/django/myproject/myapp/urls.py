from django.urls import path
from . import views

urlpatterns=[
    path("<int:id>/",view=views.sample)
]
