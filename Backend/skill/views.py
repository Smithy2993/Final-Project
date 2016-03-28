# skill views.py

# Import shortcuts for rendering and the httpresponse
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext
from skill.forms import skillForm
from django.core.context_processors import csrf

def index(request):
     context_dict = {'boldmessage': "student skills"}
     
     return render(request, 'skill/index.html', context_dict)

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
