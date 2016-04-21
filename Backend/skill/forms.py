# skill forms.py

# Import forms
# Import the skill model
from django import forms
from skill.models import skill

class skillForm(forms.ModelForm):
        
        class Meta:
                model = skill
                fields = "student_ID","name", "additional"
                exclude = ['student_ID']
