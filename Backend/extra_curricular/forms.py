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
         

        class Meta:
                model = extra_curricular
                fields = ['type_of_exp','name','role','start_date','end_date','Location','Description',]
                exclude = ['student_ID']

