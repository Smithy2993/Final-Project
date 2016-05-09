# student views.py

# Import rendering and httpresponse
# Also import student model
from django.shortcuts import render
from django.http import HttpResponse
from student.models import student
from extra_curricular.models import extra_curricular
from module.models import module
from skill.models import skill
from django.contrib.auth.models import User

# Information box displayed on each page  
def index(request, username):
    user = User.objects.get(username=username)
    person = student.objects.get(user=user)
    return render(request, 'student/home.html', {"person":person})

#Profile page information. Take's in the username argument and matches it with the students records
def profile(request, username):
        user = User.objects.get(username=username)
        person = student.objects.get(user=user)
        experience = extra_curricular.objects.filter(student_ID=person)
        modules = module.objects.filter(student_ID=person)
        skills = skill.objects.filter(student_ID=person)
        return render(request, 'student/profile.html', {"person":person, "experience":experience, "modules":modules, "skills":skills})

        

        

  
