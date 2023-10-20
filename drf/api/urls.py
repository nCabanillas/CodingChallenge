from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter() 
router.register(r'departments',views.DepartmentsViewSet)
router.register(r'employees',views.EmployeesViewSet)
router.register(r'jobs',views.JobsViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('upload_departments', views.DepartmentsUploadView.as_view(), name='uploadDepartments'),
    path('upload_employees', views.EmployeesUploadView.as_view(), name='uploadEmployees'),
    #path('upload_jobs', views.JobsUploadView.as_view(), name='uploadJobs'),
]