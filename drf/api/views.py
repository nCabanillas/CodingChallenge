#from django.shortcuts import render

from rest_framework import viewsets
from .serializer import DepartmentsSerializer
from .models import Departments

# Create your views here.

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer