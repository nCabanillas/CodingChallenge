from django.contrib import admin
from .models import Departments, Employees, Jobs
# Register your models here.

admin.site.register(Departments)
admin.site.register(Employees)
admin.site.register(Jobs)