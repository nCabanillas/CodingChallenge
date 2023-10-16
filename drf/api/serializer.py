from rest_framework import serializers
from .models import Employees, Jobs, Departments

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        #fields = ('id','department')
        fields = '__all__'