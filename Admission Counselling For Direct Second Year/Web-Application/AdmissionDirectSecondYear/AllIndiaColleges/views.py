from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def allIndiaCollege(request):
    return HttpResponse("All-India-Colleges-2019");

def allIndiaCollege2018(request):
    return HttpResponse("All-India-Colleges-2018");
