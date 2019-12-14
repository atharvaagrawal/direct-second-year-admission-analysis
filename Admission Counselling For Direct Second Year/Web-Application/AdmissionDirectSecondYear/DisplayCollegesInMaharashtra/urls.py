from django.urls import path
from . import views

urlpatterns = [
    path('Display-Colleges-In-Maharashtra/',views.display_colleges_in_maharashtra,name="display_colleges_in_maharashtra")
]
