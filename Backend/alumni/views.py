#Alumni views.py

#Import shortcuts, rendering and Httpresponse for the template purposes
#Also import the alumni forms from forms.py
#Also csrf for security purposes
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext
from alumni.forms import Find_AlumniForm
from django.core.context_processors import csrf
    
def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'alumni/index.html', context_dict)

#Find the alumni view method. This aims to search through the alumni records in the database
#It will then return the results of the query to the user
def Find_Alumni(request):
        if request.method == 'POST':
                form = Find_AlumniForm(request.POST)
                
                if form.is_valid():
                        form.save(commit=True)
                        return index(request)
                        
                else:
                        print (form.errors)

        else:
                form = Find_AlumniForm()
        return render(request, 'alumni/Find_Alumni.html', {'form': form}, RequestContext(request))
