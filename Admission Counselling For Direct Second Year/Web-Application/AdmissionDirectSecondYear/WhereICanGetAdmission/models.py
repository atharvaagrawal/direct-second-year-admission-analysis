from django.db import models

# Create your models here.


class WhereAdmissionModel(models.Model):
    college_name  = models.CharField(max_length=300)
    branch  = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    category = models.CharField(max_length=300)
    seat_type = models.CharField(max_length=300)
    min_percentage = models.FloatField()
 
    class Meta:
        db_table = "CollegeRange2019" 