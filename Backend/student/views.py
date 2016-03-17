from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("student says hey there world!")

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'student/home.html', context_dict)
    
def infobox(request):
        info = student.objects.get(student_ID,first_name,last_name,year,degree)
        student = {
        "student_info: " : info
        }
        print (info)
        return render_to_response('student/home.html', info)
