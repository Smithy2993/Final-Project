from django.db import models
from student.models import student
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import IntegerField, Model

class module(models.Model):
        MODULE_NAME = (
        ('COMP1212', 'Computer Processors'),
        ('COMP1211', 'Computer Architecture'),
        ('COMP1511', 'Introduction to Discrete Mathematics'),
        ('COMP1711', 'Procedural Programming'),
        ('COMP1911', 'Professional Computing'),
        ('COMP1121', 'Databases'),
        ('COMP1421', 'Fundamental Mathematical Concepts'),
        ('COMP1721', 'Object Oriented Programming'),
        ('COMP1921', 'Programming Project'),
        ('COMP2211', 'Operating Systems'),
        ('COMP2321', 'Formal Language and Finite Automata'),
        ('COMP2611', 'Artificial Intelligence'),
        ('COMP2931', 'Software Engineering'),
        ('COMP2221', 'Networks'),
        ('COMP2811', 'User Interfaces'),
        ('COMP2711', 'Algorithms and Data Structures I'),
        ('COMP3860', 'Research Project'),
        ('COMP3111', 'Data Science'),
        ('COMP3811', 'Computer Graphics'),
        ('COMP3911', 'Secure Computing'),
        ('COMP3223', 'Cryptography'),
        ('COMP3736', 'Information Visualization'),
        ('COMP3011', 'Web Services and Web Data'),
        ('COMP3940', 'Graph Algorithms and Complexity Theory'),
        ('COMP3910', 'Combinatorial Optimisation'),
        ('COMP3211', 'Distributed Systems'),
        ('COMP3222', 'Mobile Application Development'),
        ('COMP3321', 'Programming Languages and Compilation'),
        ('COMP3771', 'User Adaptive Intelligent Systems'),
        ('COMP3631', 'Robotics'),
        )
        CREDITS = (
        ('10', '10'),
        ('20', '20'),
        ('60', '60'),
        )
        
        student_ID = models.ForeignKey(student, default=000000000, verbose_name="Student ID")
        name = models.CharField(max_length=128, choices=MODULE_NAME)
        credits = models.CharField(max_length=2, choices=CREDITS)
        results = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
        
        def __str__(self):
                return self.name
