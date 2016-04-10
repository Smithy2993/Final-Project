#Alumni models.py

#Import the models function along with appropriate validators
from django.db import models
from django.core.validators import *

class alumni(models.Model):
        #Choices implemented within the models for degree, faculty, sector and employment
        DEGREE = (
        ('IT', 'IT'),
        ('CS', 'Computer Science'),
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
        ('ACC','Accountancy, banking and finance'),
        ('BUS','Business, consulting and management'),
        ('CHA','Charity and voluntary work'),
        ('CRE','Creative arts and design'),
        ('ENE','Energy and utilities'),
        ('ENG','Engineering and manufacturing'),
        ('ENV','Environment and agriculture'),
        ('HEA','Healthcare'),
        ('HOS','Hospitality and events management'),
        ('IT','Information technology'),
        ('LAW','Law'),
        ('LES','Law enforcement and security'),
        ('LST','Leisure, sport and tourism'),
        ('MAP','Marketing, advertising and PR'),
        ('MI','Media and internet'),
        ('PC','Property and construction'),
        ('PSA','Public services and administration'),
        ('RHR','Recruitment and HR'),
        ('SR','Sales and Retail'),
        ('SP','Science and pharmaceuticals'),
        ('SC','Social care'),
        ('TE','Teaching and education'),
        ('TL','Transport and logistics'),
        )
        EMPLOY = (
        ('Yes','Yes'),
        ('No','No'),
        )
        
        
        #Model for Alumni will have these attributes within the django database
        first_name = models.CharField(max_length=128)
        last_name = models.CharField(max_length=128)
        course = models.CharField(max_length=30, choices=DEGREE)
        faculty = models.CharField(max_length=60, choices=FACULTY)
        sector = models.CharField(max_length=60, choices=SECTOR)
        self_employed = models.CharField(max_length=3, choices=EMPLOY)

