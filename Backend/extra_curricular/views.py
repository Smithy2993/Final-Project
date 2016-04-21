# extra_curricular views.py

# Import shortcuts modules aswell as the http responses
# Import the templates and the extra_curricular forms
# Import csrf for security purposes
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from extra_curricular.forms import extra_curricularForm
from extra_curricular.models import extra_curricular
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from student.models import student

# Information box displayed on each page  
def index(request, username):
    user = student.views.index(username=username)
    person = student.objects.get(user=user)
    return render(request, 'extra_curricular/add_experience.html', {"person":person})

# Add extra_curricular method
def add_extra_curricular(request, username):

    user = User.objects.get(username=username)
    person = student.objects.get(user=user)

    if request.method == 'POST':
        form = extra_curricularForm(request.POST)
        context_dict = {'person': person, 'form':form}
        
        
        if form.is_valid():
                #form.fields['student_ID'].initial = person.student_ID
                cleaned = form.save(commit=False)
                cleaned.student_ID = student.objects.get(user=user)
                cleaned.save()
                return render(request, 'student/home.html', {"person":person})
        else:
            print (form.errors)

    else:
        form = extra_curricularForm()
        context_dict = {'person': person, 'form':form}    
    return render_to_response('extra_curricular/add_experience.html', context_dict, RequestContext(request))
        
def edit_extra_curricular(request, username):
        user = User.objects.get(username=username)
        person = student.objects.get(user=user)
        return render(request, 'extra_curricular/edit_experience.html', {"person":person})
    
def delete_extra_curricular(request, username):
    user = User.objects.get(username=username)
    person = student.objects.get(user=user)
    return render(request, 'extra_curricular/delete_experience.html', {"person":person})
                        
                        
                 
