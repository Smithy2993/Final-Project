#Alumni views.py

#Import shortcuts, rendering and Httpresponse for the template purposes
#Also import the alumni forms from forms.py
#Also csrf for security purposes
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext
from alumni.models import alumni
from student.models import student
from django.contrib.auth.models import User
from django.template.context_processors import csrf
import operator
from django.db.models import Q
    
def show_alumni(request):
        alumni_records = alumni.objects.all()
        return render(request, 'alumni/Find_Alumni.html', {'alumni_records':alumni_records})


def search_alumni(request):
        search_query = request.GET.get('search_box', None)
        results_first_name = alumni.objects.filter(first_name__contains=search_query)
        results_last_name = alumni.objects.filter(last_name__contains=search_query)
        result = result_first_name | result_second_name
        print (search_query)
        
        


                        
        
