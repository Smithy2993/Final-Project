from django.shortcuts import render
from django.http import HttpResponse

def user(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'user/index.html', context_dict)
    

