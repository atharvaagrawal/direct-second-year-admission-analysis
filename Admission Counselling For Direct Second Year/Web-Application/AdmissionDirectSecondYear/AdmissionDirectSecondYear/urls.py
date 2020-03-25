"""AdmissionDirectSecondYear URL Configuration
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls import  url 
from . import views 
from django.views.generic import TemplateView  

urlpatterns = [
    path('',include('AllIndiaColleges.urls')),  
    path('',include('DisplayCollegesInMaharashtra.urls')),
    path('',include('TopColleges.urls')),
    path('',include('TopMaharashtraCollegeList.urls')),
    path('',include('WhereICanGetAdmission.urls')),
    path('admin/', admin.site.urls), 
    path('',views.home_page,name="home"),


]

'''
    url('All-India-Colleges/', TemplateView.as_view(template_name='all_india_college.html'),name='all_india_college'), 
    url('Top-Maharashtra-College/', TemplateView.as_view(template_name='top_college_of_maharashtra.html'),name='top_maharashta_college'),
    url('Show-Seat-Matrix/', TemplateView.as_view(template_name='show_seat_matrix.html'),name='show_seat_matrix'),
    url('Top-Colleges/', TemplateView.as_view(template_name='top_colleges.html'),name='top_colleges'),
    url('College-I-Can-Get-Admission/', TemplateView.as_view(template_name='college_i_can_get_admission.html'),name='college_i_can_get'),
    url('Cut-Off-List/', TemplateView.as_view(template_name='cut_off_list.html'),name='cut_off_list'),
    url('Display-Colleges-In-Maharashtra/', TemplateView.as_view(template_name='display_colleges_in_maharashtra.html'),name='display_colleges_in_maharashtra'),

'''