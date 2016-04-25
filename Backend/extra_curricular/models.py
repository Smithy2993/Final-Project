# extra_curricular models.py

# Import models from the database
# Import validators and the student model
from django.db import models
from django.core.validators import *
from student.models import student
import datetime, random
from random import randrange

def rand_key(size):
        return ''.join([random.choice(string.letters + string.digits) for i in range(size)])
        
CHARS = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
LEN = 8
MAX_TRIES = 1024


# extra_curricular model for data input
class extra_curricular(models.Model):
        EXP = (
        ('Work', 'Work Experience'),
        ('Society', 'Society Experience'),
        ('Volunteering', 'Volunteering Experience'),
        )
        
        student_ID = models.ForeignKey(student, verbose_name="Student ID")
        identifier = models.CharField(max_length=LEN, unique=True, default=None, primary_key = True)
        type_of_exp = models.CharField(verbose_name="Type of experience", max_length=12, choices=EXP)
        name = models.CharField(max_length=128, verbose_name="Name")
        role = models.CharField(max_length=128, verbose_name="Role")
        start_date = models.DateField(("Start Date"), blank=True, null=False)
        end_date = models.DateField(("End date"), blank=True, null=False)
        Location = models.CharField(max_length=128, verbose_name="Location")
        Description = models.TextField(validators=[MaxLengthValidator(200)], verbose_name="Description")
        slug = models.SlugField(max_length=255)
        
        def save(self, *args, **kwargs):
                loop_num = 0
                unique = False
                while not unique:
                    if loop_num < MAX_TRIES:
                        new_code = ''
                        for i in range(LEN):
                            new_code += CHARS[randrange(0, len(CHARS))]
                        if not extra_curricular.objects.filter(identifier=new_code):
                            self.identifier = new_code
                            unique = True
                        loop_num += 1
                    else:
                        raise ValueError("Couldn't generate a unique code.")
                super(extra_curricular, self).save(*args, **kwargs)


        
        def __str__(self):
                return self.name
