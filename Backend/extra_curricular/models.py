from django.db import models
from django.core.validators import *
from student.models import student
import datetime

class extra_curricular(models.Model):
        EXP = (
        ('WE', 'Work Experience'),
        ('SE', 'Society Experience'),
        ('VE', 'Volunteering Experience'),
        )
        
        student_ID = models.OneToOneField(student, verbose_name="Student ID")
        type_of_exp = models.CharField(verbose_name="Type of experience", max_length=2, choices=EXP)
        name = models.CharField(max_length=128, verbose_name="Name")
        role = models.CharField(max_length=128, verbose_name="Role")
        start_date = models.DateField(("Start Date"), blank=True, null=False)
        end_date = models.DateField(("End date"), blank=True, null=False)
        Location = models.CharField(max_length=128, verbose_name="Location")
        Description = models.TextField(validators=[MaxLengthValidator(200)], verbose_name="Description")
