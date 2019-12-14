from django.shortcuts import render
from . models import ShowSeatMatrixModel
from django.db import connection

# Create your views here.
 
def show_seat_matrix(request):
    cursor = connection.cursor()
    cursor.execute('select distinct main_group from seatalloatment2019')
    row = cursor.fetchall()
    main_list = [item for i in row for item in i]


    cursor.execute('select distinct sub_group from seatalloatment2019')
    row = cursor.fetchall()
    sub_list = [item for i in row for item in i]

    cursor.execute('select distinct institute_name from seatalloatment2019')
    row = cursor.fetchall()
    institute_list = [item for i in row for item in i]

    sub_get = ""
    main_get = ""
    institute_get = ""

    result = zip() 
    if request.method == "POST":
        if request.POST.get("Vise"):    
            sub_get = request.POST['sub']
            main_get = request.POST['main']
            institute_get = request.POST['institute']

        if institute_get != "Select Institute":
            result =  ShowSeatMatrixModel.objects.raw("select * from seatalloatment2019 where institute_name = %s  & sub_group = %s & main_group = %s order by institute_name  ",(institute_get,sub_get,main_get,))
        elif main_get != "Select MainGroup":
            result =  ShowSeatMatrixModel.objects.raw("select * from seatalloatment2019 where sub_group = %s & main_group = %s order by institute_name  ",(sub_get,main_get,))


        if request.POST.get("All"):
             result =  ShowSeatMatrixModel.objects.raw("select  * from seatalloatment2019 order by sub_group")

    return render(request,'show_seat_matrix.html',{'institute_list':institute_list,'sub_list':sub_list,'main_list':main_list,'result':result})


   