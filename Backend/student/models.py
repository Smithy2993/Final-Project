from django.db import models
from django.core.validators import *
class student(models.Model):
        YEARS = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        )
        GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
        
        #student_ID = models.CharField(primary_key=True,max_length=9,validators=[RegexValidator(r'^\d{1,9}$')], unique = True)
        student_ID = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(999999999),])
        first_name = models.CharField(max_length=128)
        middle_name = models.CharField(max_length=128)
        last_name = models.CharField(max_length=128)
        gender = models.CharField(max_length=1, choices=GENDER)
        year = models.CharField(max_length=1, choices=YEARS)
        degree = models.CharField(max_length=128)
        photo = models.ImageField(upload_to="profile_pictures", null=True, blank=True)
        
