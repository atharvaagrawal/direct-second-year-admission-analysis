from django.urls import path
from . import views

urlpatterns = [
    path('Top-Colleges/',views.top_colleges,name="top_colleges")
]
