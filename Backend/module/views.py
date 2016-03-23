# module views.py

# Import rendering and httpresponse
from django.shortcuts import render
from django.http import HttpResponse

#Deafult view for the module model
def index(request):
        context_dict = {'boldmessage': "Your modules grades are:"}

        return render(request, 'module/index.html', context_dict)
