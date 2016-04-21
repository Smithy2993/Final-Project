#Module models.py

#Import models from the db aswell as the student model for connection
# Import validators and db.models fields
from django.db import models
from student.models import student
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import IntegerField, Model

class module(models.Model):
        #Choices for modules and credits per module
        MODULE_NAME = (
        ('Computer Processors', 'Computer Processors'),
        ('Computer Architecture', 'Computer Architecture'),
        ('Introduction to Discrete Mathematics', 'Introduction to Discrete Mathematics'),
        ('Procedural Programming', 'Procedural Programming'),
        ('Professional Computing', 'Professional Computing'),
        ('Databases', 'Databases'),
        ('Fundamental Mathematical Concepts', 'Fundamental Mathematical Concepts'),
        ('Object Oriented Programming', 'Object Oriented Programming'),
        ('Programming Project', 'Programming Project'),
        ('Operating Systems', 'Operating Systems'),
        ('Formal Language and Finite Automata', 'Formal Language and Finite Automata'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Software Engineering', 'Software Engineering'),
        ('Networks', 'Networks'),
        ('User Interfaces', 'User Interfaces'),
        ('Algorithms and Data Structures I', 'Algorithms and Data Structures I'),
        ('Research Project', 'Research Project'),
        ('Data Science', 'Data Science'),
        ('Computer Graphics', 'Computer Graphics'),
        ('Secure Computing', 'Secure Computing'),
        ('Cryptography', 'Cryptography'),
        ('Information Visualization', 'Information Visualization'),
        ('Web Services and Web Data', 'Web Services and Web Data'),
        ('Graph Algorithms and Complexity Theory', 'Graph Algorithms and Complexity Theory'),
        ('Combinatorial Optimisation', 'Combinatorial Optimisation'),
        ('Distributed Systems', 'Distributed Systems'),
        ('Mobile Application Development', 'Mobile Application Development'),
        ('Programming Languages and Compilation', 'Programming Languages and Compilation'),
        ('User Adaptive Intelligent Systems', 'User Adaptive Intelligent Systems'),
        ('Robotics', 'Robotics'),
        )
        CREDITS = (
        ('10', '10'),
        ('20', '20'),
        ('60', '60'),
        )
        
        #Attributes for the module model
        student_ID = models.ForeignKey(student, default=000000000, verbose_name="Student ID")
        name = models.CharField(max_length=128, choices=MODULE_NAME)
        credits = models.CharField(max_length=2, choices=CREDITS)
        results = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
        
        def __str__(self):
                return self.name
