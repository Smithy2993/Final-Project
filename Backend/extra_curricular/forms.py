# extra_curricular forms.py

# Import forms
# Import the extra_curricular model
#Import validators aswell as the datetime function
from django import forms
from django.core.validators import *
from extra_curricular.models import extra_curricular
import datetime

#Model for extra_curricular information input
class extra_curricularForm(forms.ModelForm):
        EXP = (
        ('WE', 'Work Experience'),
        ('SE', 'Society Experience'),
        ('VE', 'Volunteering Experience'),
        )
        
        type_of_exp = forms.CharField(max_length=2, widget=forms.Select(choices=EXP))
        name = forms.CharField(max_length=128)
        role = forms.CharField(max_length=128)
        start_date = forms.DateField(("Start Date"), initial=datetime.date.today)
        end_date = forms.DateField(initial=datetime.date.today)
        Location = forms.CharField(max_length=128)
        Description = forms.CharField(validators=[MaxLengthValidator(200)], widget = forms.Textarea)

        class Meta:
                model = extra_curricular
                fields = "type_of_exp","name"

