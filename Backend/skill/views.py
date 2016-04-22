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
    skills = skill.objects.filter(student_ID=person).order_by('name')

    if request.method == 'POST':
        form = skillForm(request.POST)
        context_dict = {'person': person, "skills":skills, 'form':form}
        
        
        if form.is_valid():
                #form.fields['student_ID'].initial = person.student_ID
                cleaned = form.save(commit=False)
                cleaned.student_ID = student.objects.get(user=user)
                cleaned.save()
                return render(request, 'student/home.html', {"person":person, "skills":skills})
        else:
            print (form.errors)

    else:
        form = skillForm()
        context_dict = {'person': person, "skills":skills, 'form':form}    
    return render_to_response('skill/add_skill.html', context_dict, RequestContext(request))

def index(request, username):
    user = student.views.index(username=username)
    person = student.objects.get(user=user)
    return render(request, 'skill/add_skill.html', {"person":person})

def edit_skill(request, username):
        user = User.objects.get(username=username)
        person = student.objects.get(user=user)
        return render(request, 'skill/edit_skill.html', {"person":person})
    
def delete_skill(request, username):
    user = User.objects.get(username=username)
    person = student.objects.get(user=user)
    return render(request, 'skill/delete_skill.html', {"person":person})
