from django.db import models

# Create your models here.

class Departments(models.Model):
    id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['id']
    
    def __str__(self):
        return self.department
    
class Jobs(models.Model):
    id = models.IntegerField(primary_key=True)
    job = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['id']
    
    def __str__(self):
        return self.job

class Employees(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True, auto_now_add=False)
    department_id = models.IntegerField()
    job_id = models.IntegerField()
    
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['id']
    
    def __str__(self):
        return self.name