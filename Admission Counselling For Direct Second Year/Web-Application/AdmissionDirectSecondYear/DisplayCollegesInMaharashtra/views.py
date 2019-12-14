from django.shortcuts import render
from . models import DisplayCollegesInMaharashtraModel
from django.db import connection
from django.http import HttpResponse
# Create your views here.
 
def display_colleges_in_maharashtra(request):
    cursor = connection.cursor()

    cursor.execute('select distinct course_name from collegeinmaharashtra2019')
    row = cursor.fetchall()
    course_list = [item for i in row for item in i]

    cursor.execute('select distinct college_name from collegeinmaharashtra2019')
    row = cursor.fetchall()
    college_list = [item for i in row for item in i]

    college_get = ""
    course_get = ""
    result = zip() 

    if request.method == "POST":
        if request.POST.get("Vise"):    
            college_get = request.POST['college']
            course_get = request.POST['course']
        
        if college_get != "Select College":
            result =  DisplayCollegesInMaharashtraModel.objects.raw("select * from collegeinmaharashtra2019 where college_name = %s order by college_name  ",(college_get,))
        elif course_get != "Select Course":
            result =  DisplayCollegesInMaharashtraModel.objects.raw("select * from collegeinmaharashtra2019 where course_name = %s order by college_name ",(course_get,))


        if request.POST.get("All"):
             result =  DisplayCollegesInMaharashtraModel.objects.raw("select  * from collegeinmaharashtra2019 order by college_name")
        
    
    return render(request,'display_colleges_in_maharashtra.html',{'course_list':course_list,'college_list':college_list,'result':result})



   