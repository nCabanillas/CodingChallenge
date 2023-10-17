from rest_framework import serializers
from .models import Employees, Jobs, Departments

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        #fields = ('id','department')
        fields = '__all__'
        
class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'