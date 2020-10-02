from django.shortcuts import render
from . models import WhereAdmissionModel
from django.db import connection
# Create your views here.

def college_i_can_get_admission(request):
     
    cursor = connection.cursor()
    cursor.execute('select distinct college_name from collegerange2019')
    row = cursor.fetchall()
    college_list = [item for i in row for item in i]

    cursor.execute('select distinct category from collegerange2019')
    row = cursor.fetchall()
    category_list = [item for i in row for item in i]
    
    cursor.execute('select distinct branch from collegerange2019')
    row = cursor.fetchall()
    branch_list = [item for i in row for item in i]

    category_get = ""
    college_get = ""
    branch_get = ""
    percentage_get = ""

    result = zip() 
    if request.method == "POST":
        if request.POST.get("Vise"):    
            category_get = request.POST['category']
            branch_get = request.POST['branch']
            college_get = request.POST['college']
            percentage_get = str(request.POST['percentage'])

        if percentage_get !='0' and college_get != "Select College Name" and category_get != "Select Category":
            result = WhereAdmissionModel.objects.raw("select * from collegerange2019 where min_percentage <= %s AND college_name = %s AND category = %s order by college_name", (percentage_get,college_get,category_get))
        elif college_get != "Select College Name":
            result =  WhereAdmissionModel.objects.raw("select * from collegerange2019 where college_name = %s  order by category  ",(college_get,))
        elif category_get != "Select Category":
            result =  WhereAdmissionModel.objects.raw("select * from collegerange2019 where category = %s order by college_name ",(category_get,))
        elif percentage_get !=0:
            result = WhereAdmissionModel.objects.raw("select * from collegerange2019 where min_percentage <= %s order by college_name ", (percentage_get,))
           
        
        if request.POST.get("All"):
            result =  WhereAdmissionModel.objects.raw("select  * from collegerange2019 order by college_name,category")
    return render(request,'college_i_can_get_admission.html',{'college_list':college_list,'category_list':category_list,'branch_list':branch_list,'result':result})
  
