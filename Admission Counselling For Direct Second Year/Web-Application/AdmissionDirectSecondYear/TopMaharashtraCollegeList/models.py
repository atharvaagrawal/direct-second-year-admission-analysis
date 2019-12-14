from django.db import models

# Create your models here.


class TopMaharashtraCollegeListModel(models.Model):
    college_name = models.CharField(max_length=300)
    merit_no = models.IntegerField()
    marks = models.FloatField()
    app_id = models.CharField(max_length=300)
    name  = models.CharField(max_length=300)
    gender  = models.CharField(max_length=300)
    category  = models.CharField(max_length=300)
    seat_type  = models.CharField(max_length=300)
   
    class Meta:
        db_table = "Allocated2019" 