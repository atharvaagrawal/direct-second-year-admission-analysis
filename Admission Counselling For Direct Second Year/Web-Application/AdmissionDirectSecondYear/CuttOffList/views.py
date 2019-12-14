from django.shortcuts import render
from . models import CuttOffListModel
from django.db import connection
# Create your views here.

def cut_off_list(request):
    cursor = connection.cursor()

    cursor.execute('select distinct course_name from cuttofflist2019')
    row = cursor.fetchall()
    course_list = [item for i in row for item in i]

    cursor.execute('select distinct shift from cuttofflist2019')
    row = cursor.fetchall()
    shift_list = [item for i in row for item in i]

    cursor.execute('select distinct institute_name from cuttofflist2019')
    row = cursor.fetchall()
    institute_list = [item for i in row for item in i]

    course_get = ""
    shift_get = ""
    institute_get = ""
    result = zip() 
    if request.method == "POST":
        if request.POST.get("Vise"):    
            course_get = request.POST['course']
            shift_get = request.POST['shift']
            institute_get = request.POST['institute']

        if institute_get != "Select Institute":
            result =  CuttOffListModel.objects.raw("select * from cuttofflist2019 where institute_name = %s  & course_name = %s & shift = %s order by gopen  ",(institute_get,course_get,shift_get,))
        elif course_get != "Select Course":
            result =  CuttOffListModel.objects.raw("select * from cuttofflist2019 where course_name = %s & shift = %s order by gopen  ",(course_get,shift_get,))


        if request.POST.get("All"):
             result =  CuttOffListModel.objects.raw("select  * from cuttofflist2019 order by course_name")

    return render(request,'cut_off_list.html',{'institute_list':institute_list,'shift_list':shift_list,'course_list':course_list,'result':result})

