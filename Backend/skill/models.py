# skill models.py
#Import the models from the db
from django.db import models
from student.models import student
from django.core.validators import *
import random, uuid
from random import randrange

#Skills have all these attributes
class skill(models.Model):
        student_ID = models.ForeignKey(student, verbose_name="Student ID")
        identifier = models.CharField(max_length=8, unique=True, default=None, primary_key = True)
        name = models.CharField(max_length=128, blank = False)
        additional = models.TextField(validators=[MaxLengthValidator(200)], verbose_name="Additional information", blank = True)
        
        def save(self, *args, **kwargs):
            if not (self.identifier):
                self.identifier = uuid.uuid4().hex[:8].upper()
            super(skill, self).save(*args, **kwargs)

        
        def __str__(self):
                return self.name
