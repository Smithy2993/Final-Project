from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("student says hey there world!")

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'student/index.html', context_dict)
