#Import the models from the db
from django.db import models

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

        student_ID = models.ForeignKey('student.student')
        name = models.CharField(max_length=128, choices=SKILLS)
