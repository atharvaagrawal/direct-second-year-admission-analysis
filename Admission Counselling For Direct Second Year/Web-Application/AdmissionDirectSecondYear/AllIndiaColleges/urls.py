from django.urls import path
from . import views

urlpatterns = [
    path('All-India-Colleges/',views.all_india_college,name="all_india_college")
    
]
  