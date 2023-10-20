
from rest_framework import viewsets
from .serializer import DepartmentsSerializer, EmployeesSerializer, JobsSerializer
from .models import Departments, Employees, Jobs

from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response

import pandas as pd

# Views
class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    
class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

class EmployeesUploadView(APIView):
    def post(self, request,*args ,**kwargs):
        file_obj = request.data['file'] #Json send by post request
        columns_name = ['id','name','datetime','department_id','job_id']
        df = pd.read_csv(file_obj, names=columns_name)

        df['job_id'] = df['job_id'].fillna(0) #la columna 'job_id' reemplazamos quitar NaN 
        df['department_id'] = df['department_id'].fillna(0) #la columna 'job_id' reemplazamos quitar NaN 
        
        try:
            for idx in df.index:
                id = df.iloc[idx]['id']
                name = df.iloc[idx]['name']
                datetime = df.iloc[idx]['datetime']
                department_id = df.iloc[idx]['department_id']
                job_id = df.iloc[idx]['job_id']
                print(f'DATA: id = {id} , name = {name}, datetime = {datetime}, department_id = {department_id}, job_id = {job_id}')

                object = Employees(id=id, name=name, datetime = datetime, department_id = department_id, job_id = job_id)
                object.save()

        except Employees.DoesNotExist:
            return Response({'message': 'Object not found'}, status=404)

        return Response({"message": "DataFrame received and processed successfully"})

class DepartmentsUploadView(APIView):
    def post(self, request,*args ,**kwargs):
        file_obj = request.data['file'] #Json send by post request
        columns_name = ['id','department']
        df = pd.read_csv(file_obj, names=columns_name)
        
        try:
            for idx in df.index:
                id = df.iloc[idx]['id']
                department = df.iloc[idx]['department']
                print(f'DATA: id = {id} , departamento = {department}')

                object = Departments(id=id, department=department)
                object.save()

        except Departments.DoesNotExist:
            return Response({'message': 'Object not found'}, status=404)

        return Response({"message": "DataFrame received and processed successfully"})

class JobsUploadView(APIView):
    def post(self, request,*args ,**kwargs):
        file_obj = request.data['file'] #Json send by post request
        columns_name = ['id','job']
        df = pd.read_csv(file_obj, names=columns_name)

        try:
            for idx in df.index:
                id = df.iloc[idx]['id']
                job = df.iloc[idx]['job']
                print(f'DATA: id = {id} , job = {job}')

                object = Jobs(id=id, job=job)
                object.save()

        except Departments.DoesNotExist:
            return Response({'message': 'Object not found'}, status=404)

        return Response({"message": "DataFrame received and processed successfully"})