# libraries for importing
from import_export import resources
# libraries to render a httpsresponse
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .serializer import DepartmentsSerializer, EmployeesSerializer, JobsSerializer
from .models import Departments, Employees, Jobs

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
    parser_classes = [JSONParser]
    
    def post(self, request,*args ,**kwargs):
        data = request.data #Json send by post request
        df = pd.DataFrame(data)
    
        try:
            for idx in df.index:
                id = df.iloc[idx]['id']
                name = df.iloc[idx]['name']
                # datetime = df.iloc[idx]['datetime']
                # department_id = df.iloc[idx]['department_id']
                # job_id = df.iloc[idx]['job_id']
                # print(f'DATA: id = {id} , name = {name}, datetime={datetime}, departamento_id = {department_id}, job_id = {job_id}')
                print( id, name)
                # object = Employees(id=id, name=name, datetime=datetime, department_id=department_id, job_id=job_id)
                # object.save()
                
        except Employees.DoesNotExist:
            return Response({'message': 'Object not found'}, status=404)
    
        return Response({"message": "DataFrame received and processed successfully","data":df})