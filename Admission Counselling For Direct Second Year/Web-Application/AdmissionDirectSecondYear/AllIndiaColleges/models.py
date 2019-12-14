from django.db import models

# Create your models here.

class AllIndiaCollegeModel(models.Model):
    name = models.CharField(max_length=300)
    city  = models.CharField(max_length=300)
    state  = models.CharField(max_length=300)
    class Meta:
        db_table = "ALLINDIACOLLEGE2019" 

 