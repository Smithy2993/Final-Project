#Alumni form.py

#Import the model alongside the django forms and validators
from django import forms
from django.core.validators import *
from alumni.models import alumni

#The alumni form class. Attributes within the form are listed here
class Find_AlumniForm(forms.ModelForm):
        #Choices implemented within the models for degree, faculty, sector and employment
        #Used for drop down menu's with a list of choices for each option
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
        
        #Models for the form. Alumni will have these attributes within the django database
        #Validation is called from the model and is therefore uneeded within the form
        first_name = forms.CharField(max_length=128)
        last_name = forms.CharField(max_length=128)
        course = forms.CharField(max_length=30, widget=forms.Select(choices=DEGREE))
        faculty = forms.CharField(max_length=60, widget=forms.Select(choices=FACULTY))
        sector = forms.CharField(max_length=60, widget=forms.Select(choices=SECTOR))
        self_employed = forms.CharField(max_length=3, widget=forms.Select(choices=EMPLOY))
        
        #The models meta data. First name, last name,course and sector are the chosen attributes
        class Meta:
                model = alumni
                fields = "first_name","last_name","course","sector"
