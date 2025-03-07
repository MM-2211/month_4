
from django.urls import path
from . import views

urlpatterns = [
    path("text/", views.text),
    path("animal/", views.animal),
    path("time/", views.time)
]