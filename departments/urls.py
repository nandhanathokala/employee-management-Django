from django.urls import path
from .views import department_list, add_department

urlpatterns = [
    path('', department_list, name='department_list'),
    path('add/', add_department, name='add_department'),
]
