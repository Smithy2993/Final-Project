# skill models.py
#Import the models from the db
from django.db import models
from student.models import student

#Skills have all these attributes
class skill(models.Model):
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

        student_ID = models.ForeignKey(student, verbose_name="Student ID")
        name = models.CharField(max_length=128, blank = True, choices=SKILLS)
        additional = models.CharField(max_length=128, blank = True)
        
        def __str__(self):
                return self.name
