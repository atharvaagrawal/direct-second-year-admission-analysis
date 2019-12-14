from django.db import models

# Create your models here.
 
class TopCollegesModel(models.Model):
    institute_id = models.CharField(max_length=300)
    college_name  = models.CharField(max_length=300)
    city  = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    score = models.FloatField()
    crank = models.IntegerField()

    class Meta:
        db_table = "IndiaTop200College2019" 

