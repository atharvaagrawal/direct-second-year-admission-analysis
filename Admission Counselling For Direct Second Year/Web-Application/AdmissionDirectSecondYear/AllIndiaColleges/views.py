from django.shortcuts import render
from django.http import HttpResponse
from . models import AllIndiaCollegeModel
from django.db import connection

# Create your views here.

def all_india_college(request):
    cursor = connection.cursor()

    cursor.execute('select distinct state from allindiacollege2019')
    row = cursor.fetchall()
    state_list = [item for i in row for item in i]

    cursor.execute('select distinct city from allindiacollege2019')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]

    city_get = ""
    state_get = ""
    result = zip() 
    if request.method == "POST":
        if request.POST.get("Vise"):    
            city_get = request.POST['city']
            state_get = request.POST['state']
        
        if city_get != "Select City":
            #cursor.execute("select * from allindiacollege2019 where city = %s ",(city_get,))
            result =  AllIndiaCollegeModel.objects.raw("select * from allindiacollege2019 where city = %s order by state  ",(city_get,))
        elif state_get != "Select State":
            #cursor.execute("select * from allindiacollege2019 where state = %s ",(state_get,))
            result =  AllIndiaCollegeModel.objects.raw("select * from allindiacollege2019 where state = %s order by city ",(state_get,))


        if request.POST.get("All"):
             result =  AllIndiaCollegeModel.objects.raw("select  * from allindiacollege2019 order by state")
        #result = cursor.fetchall()
    
    return render(request,'all_india_college.html',{'city_list':city_list,'state_list':state_list,'result':result})




