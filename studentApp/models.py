from django.db import models
class Student(models.Model):
    name         =  models.CharField(max_length=25)
    email        =  models.EmailField(max_length=40)
    phone        =  models.IntegerField()
    section      =  models.CharField(max_length=25)
    photo        =  models.FileField(upload_to='photos')
