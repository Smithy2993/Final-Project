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
                return render(request, 'skill/skill_added.html', {"person":person, "skills":skills})
        else:
            print (form.errors)

    else:
        form = skillForm()
        context_dict = {'person': person, "skills":skills, 'form':form}    
    return render_to_response('skill/add_skill.html', context_dict, RequestContext(request))
    
   
#Show's an indepth look at the user details displaying all information for the record clicked
def show_detail(request, username, details_view_url):
        context = RequestContext(request)
        try:
                details = skill.objects.get(identifier__iexact=details_view_url)
                user = User.objects.get(username=username)
                person = student.objects.get(user=user)    
        except skill.DoesNotExist:
                pass
        return render_to_response('skill/detailed_skill.html', {'details':details, 'person':person}, context)
        

def edit_skill(request, username, details_view_url):
        context = RequestContext(request)
        try:
                details = skill.objects.get(identifier__iexact=details_view_url)
                user = User.objects.get(username=username)
                person = student.objects.get(user=user)
                if request.method == 'POST':
                    form = skillForm(request.POST, instance=details)
                    if form.is_valid():
                        form.save(commit=True)
                        return render(request, 'student/home.html', {"person":person})
                    else:
                        print (form.errors)                    
                else:
                    form = skillForm(instance=details)
        except skill.DoesNotExist:
                pass 
        return render(request, 'skill/edit_skill.html', {'person':person, 'details':details, 'form':form})





def delete_skill(request, username, details_view_url):
        context = RequestContext(request)
        user = User.objects.get(username=username)
        person = student.objects.get(user=user)
        try:
                details = skill.objects.get(identifier__iexact=details_view_url)
                details.delete()
        except skill.DoesNotExist:
                pass
        return render(request, 'skill/delete_skill.html', {'person':person,'details':details})
