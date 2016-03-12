from django.db import models

class skill(models.Model):
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
