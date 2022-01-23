# studentApp/views.py
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from studentApp.models import Student

class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    # Field must be same as the model attribute
    fields = ['name', 'email', 'phone', 'section' , 'photo']
    success_url = reverse_lazy('student_list')

class StudentUpdate(UpdateView):
    model = Student
    # Field must be same as the model attribute
    fields = ['name', 'email', 'phone', 'section' , 'photo']
    success_url = reverse_lazy('student_list')

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')

