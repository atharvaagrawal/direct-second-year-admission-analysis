from django.urls import path
from . import views

urlpatterns = [
    path('Cut-Off-List/',views.cut_off_list,name="cut_off_list")
]
