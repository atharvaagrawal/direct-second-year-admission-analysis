from django.shortcuts import render
from . models import TopMaharashtraCollegeListModel
from django.db import connection
# Create your views here.

def top_college_of_maharashtra(request):
    cursor = connection.cursor()

    cursor.execute('select distinct college_name from allocated2019')
    row = cursor.fetchall()
    college_list = [item for i in row for item in i]
    
    cursor.execute('select distinct category from allocated2019')
    row = cursor.fetchall()
    category_list = [item for i in row for item in i]

    category_get = ""
    college_get = ""
    result = zip() 
    if request.method == "POST":
        if request.POST.get("Vise"):    
            category_get = request.POST['category']
            college_get = request.POST['college']

        if college_get != "Select  College Name":
            result =  TopMaharashtraCollegeListModel.objects.raw("select * from allocated2019 where college_name = %s order by category  ",(college_get,))
        elif category_get != "Select Category":
            result =  TopMaharashtraCollegeListModel.objects.raw("select * from allocated2019 where category = %s order by college_name ",(category_get,))
        
        if request.POST.get("All"):  
            result =  TopMaharashtraCollegeListModel.objects.raw("select  * from allocated2019 order by college_name")
    return render(request,'top_college_of_maharashtra.html',{'college_list':college_list,'category_list':category_list,'result':result})

