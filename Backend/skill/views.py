# skill views.py

# Import shortcuts for rendering and the httpresponse
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext
from skill.forms import skillForm
from skill.models import skill
from student.models import student
from django.contrib.auth.models import User
from django.core.context_processors import csrf

def add_skill(request):
        
        if request.method == 'POST':
                form = skillForm(request.POST)
                
                if form.is_valid():
                        form.save(commit=True)
                        return index(request)
                        
                else:
                        print (form.errors)

        else:
                form = skillForm()
                
        return render_to_response('skill/add_skill.html', {'form': form}, RequestContext(request))

def index(request, username):
    user = student.views.index(username=username)
    skills = skill.objects.get(user=user)
    person = student.objects.get(user=user)
    
    return render(request, 'skill/add_skill.html', {"person":person},{"skill",skill})
