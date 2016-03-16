from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User	
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
        DEGREE = (
        ('IT', 'Information Technology'),
        ('CS', 'Computer Science'),
        )
        
        user = models.OneToOneField(User)
        student_ID = models.CharField(unique=True, max_length=9, validators=[RegexValidator(regex='^[0-9]{9,9}$', message='Must be 9 unique numbers', code='nomatch')])
        first_name = models.CharField(max_length=128)
        middle_name = models.CharField(max_length=128)
        last_name = models.CharField(max_length=128)
        gender = models.CharField(max_length=1, choices=GENDER)
        year = models.CharField(max_length=1, choices=YEARS)
        degree = models.CharField(max_length=2, choices=DEGREE)
        photo = models.ImageField(upload_to="profile_pictures", null=True, blank=True)
        
        
