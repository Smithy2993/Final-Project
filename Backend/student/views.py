# student views.py

# Import rendering and httpresponse
# Also import student model
from django.shortcuts import render
from django.http import HttpResponse
from student.models import student

def index(request):
    return HttpResponse("student says hey there world!")

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'student/home.html', context_dict)

# Information box displayed on each page    
def infobox(request):
        info = student.objects.get(student_ID,first_name,last_name,year,degree)
        student = {
        "student_info: " : info
        }
        print (info)
        return render_to_response('student/home.html', info)
