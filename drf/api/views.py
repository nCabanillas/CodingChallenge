#from django.shortcuts import render

from rest_framework import viewsets
from .serializer import DepartmentsSerializer, EmployeesSerializer, JobsSerializer
from .models import Departments, Employees, Jobs

# Create your views here.

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    
class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    
class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer