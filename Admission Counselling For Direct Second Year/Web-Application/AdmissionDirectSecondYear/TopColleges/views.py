from django.shortcuts import render
from . models import TopCollegesModel
from django.db import connection
# Create your views here.

def top_colleges(request):
    cursor = connection.cursor()

    cursor.execute('select distinct state from indiatop200college2019')
    row = cursor.fetchall()
    state_list = [item for i in row for item in i]

    cursor.execute('select distinct city from indiatop200college2019')
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
            result =  TopCollegesModel.objects.raw("select * from indiatop200college2019 where city = %s order by crank  ",(city_get,))
        elif state_get != "Select State":
            result =  TopCollegesModel.objects.raw("select * from indiatop200college2019 where state = %s order by crank ",(state_get,))


        if request.POST.get("All"):
             result =  TopCollegesModel.objects.raw("select  * from indiatop200college2019 order by crank")
        
    return render(request,'top_colleges.html',{'city_list':city_list,'state_list':state_list,'result':result})
