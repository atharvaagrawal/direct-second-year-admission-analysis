from django.urls import path
from . import views

urlpatterns = [
    path('Top-Maharashtra-College/',views.top_college_of_maharashtra,name="top_maharashta_college")
]
