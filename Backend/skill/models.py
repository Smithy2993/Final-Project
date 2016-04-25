# skill models.py
#Import the models from the db
from django.db import models
from student.models import student
from django.core.validators import *

#Skills have all these attributes
class skill(models.Model):
        student_ID = models.ForeignKey(student, verbose_name="Student ID")
        name = models.CharField(max_length=128, blank = False, unique = True)
        additional = models.TextField(validators=[MaxLengthValidator(200)], verbose_name="Additional information", blank = True)
        
        def __str__(self):
                return self.name
