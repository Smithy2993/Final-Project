# skill views.py

# Import shortcuts for rendering and the httpresponse
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext
from skill.forms import skillForm
from skill.models import skill
from django.contrib.auth.models import User
from student.models import student
from django.template.context_processors import csrf

def add_skill(request, username):

    user = User.objects.get(username=username)
    person = student.objects.get(user=user)

    if request.method == 'POST':
        form = skillForm(request.POST)
        context_dict = {'person': person, 'form':form}
        
        
        if form.is_valid():
                #form.fields['student_ID'].queryset = student.objects.get(id = student_ID)
                form.save(commit=True)
                return render(request, 'student/home.html', {"person":person})
        else:
            print (form.errors)

    else:
        form = skillForm()
        context_dict = {'person': person, 'form':form}    
    return render_to_response('skill/add_skill.html', context_dict, RequestContext(request))

def index(request, username):
    user = student.views.index(username=username)
    person = student.objects.get(user=user)
    return render(request, 'skill/add_skill.html', {"person":person})
