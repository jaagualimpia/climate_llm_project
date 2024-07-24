from django.urls import path

from . import views

urlpatterns = [
    path("response", views.QueryBasicView.as_view(), name="index"),
]