#Alumni models.py

#Import the models function along with appropriate validators
from django.db import models
from django.core.validators import *
import random
from random import randrange

# Determines a random key for identification purposes
def rand_key(size):
        return ''.join([random.choice(string.letters + string.digits) for i in range(size)])
        
CHARS = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
LEN = 8
MAX_TRIES = 1024

# Attributes relating to each alumni object
class alumni(models.Model):
        #Choices implemented within the models for degree, faculty, sector and employment
        DEGREE = (
        ('Information Technology', 'Information Technology'),
        ('Computer Science', 'Computer Science'),
        )
        FACULTY = (
        ('Art','Faculty of Art'),
        ('Bio','Faculty of Biological Sciences'),
        ('Bus','Faculty of Business'),
        ('Eds','Faculty of Education, Social Sciences and Law'),
        ('Eng','Faculty of Engineering'),
        ('Env','Faculty of Enviroment'),
        ('Mat','Faculty of Mathematics and Physical Sciences'),
        ('Med','Faculty of Medicine and Health'),
        ('Per','Faculty of Performance, Visual Arts and Communications'),
        )
        SECTOR = (
        ('Accountancy, banking and finance','Accountancy, banking and finance'),
        ('Business, consulting and management','Business, consulting and management'),
        ('Charity and voluntary work','Charity and voluntary work'),
        ('Creative arts and design','Creative arts and design'),
        ('Energy and utilities','Energy and utilities'),
        ('Engineering and manufacturing','Engineering and manufacturing'),
        ('Environment and agriculture','Environment and agriculture'),
        ('Healthcare','Healthcare'),
        ('Hospitality and events management','Hospitality and events management'),
        ('IT','IT'),
        ('Law','Law'),
        ('Law enforcement and security','Law enforcement and security'),
        ('Leisure, sport and tourism','Leisure, sport and tourism'),
        ('Marketing, advertising and PR','Marketing, advertising and PR'),
        ('Media and internet','Media and internet'),
        ('Property and construction','Property and construction'),
        ('Public services and administration','Public services and administration'),
        ('Recruitment and HR','Recruitment and HR'),
        ('Sales and Retail','Sales and Retail'),
        ('Science and pharmaceuticals','Science and pharmaceuticals'),
        ('Social care','Social care'),
        ('Teaching and education','Teaching and education'),
        ('Transport and logistics','Transport and logistics'),
        )
        EMPLOY = (
        ('Yes','Yes'),
        ('No','No'),
        )
        
        
        #Model for Alumni will have these attributes within the django database
        identifier = models.CharField(max_length=LEN, unique=True, default=None, primary_key = True)
        first_name = models.CharField(max_length=128)
        last_name = models.CharField(max_length=128)
        course = models.CharField(max_length=30, choices=DEGREE)
        faculty = models.CharField(max_length=60, choices=FACULTY)
        sector = models.CharField(max_length=60, choices=SECTOR)
        email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
        self_employed = models.CharField(max_length=3, choices=EMPLOY)
        
        def save(self, *args, **kwargs):
                loop_num = 0
                unique = False
                while not unique:
                    if loop_num < MAX_TRIES:
                        new_code = ''
                        for i in range(LEN):
                            new_code += CHARS[randrange(0, len(CHARS))]
                        if not alumni.objects.filter(identifier=new_code):
                            self.identifier = new_code
                            unique = True
                        loop_num += 1
                    else:
                        raise ValueError("Couldn't generate a unique code.")
                super(alumni, self).save(*args, **kwargs)


