from django.db import models

# Create your models here.

class Departments(models.Model):
    id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=100)
    
class Jobs():
    id = models.IntegerField(primary_key=True)
    job = models.CharField(max_length=100)    

class Employees():
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    department_id = models.IntegerField(primary_key=True)
    job_id = models.IntegerField()
