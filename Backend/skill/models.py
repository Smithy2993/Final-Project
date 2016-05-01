# skill models.py
#Import the models from the db
from django.db import models
from student.models import student
from django.core.validators import *
import random
from random import randrange


def rand_key(size):
        return ''.join([random.choice(string.letters + string.digits) for i in range(size)])
        
CHARS = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
LEN = 8
MAX_TRIES = 1024

#Skills have all these attributes
class skill(models.Model):
        student_ID = models.ForeignKey(student, verbose_name="Student ID")
        identifier = models.CharField(max_length=LEN, unique=True, default=None, primary_key = True)
        name = models.CharField(max_length=128, blank = False)
        additional = models.TextField(validators=[MaxLengthValidator(200)], verbose_name="Additional information", blank = True)
        
        def save(self, *args, **kwargs):
                loop_num = 0
                unique = False
                while not unique:
                    if loop_num < MAX_TRIES:
                        new_code = ''
                        for i in range(LEN):
                            new_code += CHARS[randrange(0, len(CHARS))]
                        if not skill.objects.filter(identifier=new_code):
                            self.identifier = new_code
                            unique = True
                        loop_num += 1
                    else:
                        raise ValueError("Couldn't generate a unique code.")
                super(skill, self).save(*args, **kwargs)

        
        def __str__(self):
                return self.name
