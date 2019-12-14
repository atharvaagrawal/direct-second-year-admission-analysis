from django.urls import path
from . import views

urlpatterns = [
    path('College-I-Can-Get-Admission/',views.college_i_can_get_admission,name="college_i_can_get")
]
