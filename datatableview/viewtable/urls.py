from django.urls import path
from .views import *


urlpatterns = [
    path('employee/json',OrderListJson.as_view(), name = 'employee_list_json'),
    path('view_project/',view_project,name='view_project'),

]