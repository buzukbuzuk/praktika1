from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=0)
    surname = models.CharField(max_length=50, default=0)
    email = models.EmailField(max_length=50, null=True)
    phoneNum = models.CharField(max_length=50, null=True)
    gpa = models.FloatField(default=0)
