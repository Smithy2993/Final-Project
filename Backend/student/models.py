from django.db import models

class student(models.Model):
        Student_ID = models.PositiveIntegerField(max_length=9, unique = True)
        First_name = models.CharField(max_length=128)
        Middle_name = models.CharField(max_length=128)
        Last_name = models.CharField(max_length=128)
        Year = models.CharField(max_length=3)
        Degree_Pro = models.CharField(max_length=128)
        
