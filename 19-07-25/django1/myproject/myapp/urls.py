from django.urls import path

from . import views

urlpatterns=[
    # path("sum/",view=views.sum),
    path("post/",view=views.post_view),
    # path("",view=views.put_view),
]