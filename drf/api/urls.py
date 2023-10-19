from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter() 
router.register(r'department',views.DepartmentsViewSet)
router.register(r'employees',views.EmployeesViewSet)
router.register(r'jobs',views.JobsViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('export_csv/', views.export_csv, name='export_csv')
]