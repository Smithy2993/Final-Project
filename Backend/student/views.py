# student views.py

# Import rendering and httpresponse
# Also import student model
from django.shortcuts import render
from django.http import HttpResponse
from student.models import student
from django.contrib.auth.models import User

# Information box displayed on each page  
def index(request, username):
    user = User.objects.get(username=username)
    person = student.objects.get(user=user)
    return render(request, 'student/home.html', {"person":person})

  
