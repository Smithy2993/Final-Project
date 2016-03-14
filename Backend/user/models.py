from django.db import models

class user(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    student_ID = models.ForeignKey('student.student')

# Create your models here.
