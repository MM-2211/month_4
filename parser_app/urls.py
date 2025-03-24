from django.urls import path
from . import views

urlpatterns = [
    path("litnet_list/", views.LitnetBookListView.as_view(), name="litnet_list"),
    path("rezka_list/", views.RezkaFilmListView.as_view(), name="rezka_list"),
    path("parser_form/", views.ParserForm.as_view(), name="parser_form"),
]