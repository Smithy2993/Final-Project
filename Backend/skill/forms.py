# skill forms.py

# Import forms
# Import the skill model
from django import forms
from skill.models import skill

class skillForm(forms.ModelForm):
        #Choices so far for the name attribute. More can be added at a later date
        SKILLS=(
        ('CSS', 'CSS'),
        ('Info-security', 'Information Security'),
        ('JAVA', 'JAVA'),
        ('HTML5', 'HTML5'),
        ('Teamwork', 'Teamwork'),
        ('Networks', 'Networking'),
        ('Data security', 'Data security'),
        ('Programming', 'Programming'),
        ('C++', 'C++'),
        ('PHP', 'PHP'),
        )

        name = forms.CharField(max_length=128, widget=forms.Select(choices=SKILLS))
        additional = forms.CharField(max_length=128)
        
        class Meta:
                model = skill
                fields = "name", "additional"
