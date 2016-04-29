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
        start_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
        end_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'),input_formats=('%d/%m/%Y',))


        class Meta:
                model = extra_curricular
                fields = ['type_of_exp','name','role','start_date','end_date','Location','Description',]
                exclude = ['student_ID','identifier']
                
        def clean(self):
                cleaned_data = super(extra_curricularForm, self).clean()
                start_date = cleaned_data.get("start_date")
                end_date = cleaned_data.get("end_date")
                if end_date < start_date:
                        msg = u"End date should be greater than start date."
                        self._errors["end_date"] = self.error_class([msg])

