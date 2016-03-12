from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        context_dict = {'boldmessage': "Your modules grades are:"}

        return render(request, 'module/index.html', context_dict)

# Create your views here.
