from django.urls import path
from . import views

urlpatterns = [
    path("status/", views.status),
    path("start/", views.start),
    path("stop/", views.stop),
    path("overload/", views.overload),
    path("reset/", views.reset),
]
