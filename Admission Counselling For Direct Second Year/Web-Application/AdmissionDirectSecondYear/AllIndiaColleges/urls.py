from django.urls import path
from . import views

urlpatterns = [
    path('All-India-Colleges-2019/',views.allIndiaCollege,name="allIndiaCollege"),
    path('All-India-Colleges-2018/',views.allIndiaCollege2018,name="allIndiaCollege")
]
