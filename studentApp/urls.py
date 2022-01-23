# studentApp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentList.as_view(), name='student_list'), # url http://127.0.0.1:8000/student
    path('view/<int:pk>', StudentDetail.as_view(), name='student_detail'),
    path('new', StudentCreate.as_view(), name='student_new'), # url http://127.0.0.1:8000/student/new
    path('edit/<int:pk>', StudentUpdate.as_view(), name='student_edit'),
    path('delete/<int:pk>', StudentDelete.as_view(), name='student_delete'),
]