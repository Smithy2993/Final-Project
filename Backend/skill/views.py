# skill views.py

# Import shortcuts for rendering and the httpresponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
     context_dict = {'boldmessage': "student skills"}
     
     return render(request, 'skill/index.html', context_dict)
