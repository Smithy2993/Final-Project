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
from django.db.models import Q
import re

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):

    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]
 
def get_query(query_string, search_fields):
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
    
def show_alumni(request,username):
        user = User.objects.get(username=username)
        person = student.objects.get(user=user)
        alumni_records = alumni.objects.all().order_by('first_name')
        return render(request, 'alumni/Find_Alumni.html', {'alumni_records':alumni_records, 'person':person})
        
#Show's an indepth look at the alumnis details displaying all information for the record clicked
def show_detail(request, username, details_view_url):
        context = RequestContext(request)
        try:
                details = alumni.objects.get(identifier__iexact=details_view_url)
                user = User.objects.get(username=username)
                person = student.objects.get(user=user)   
        
        except alumni.DoesNotExist:
                pass
        return render_to_response('alumni/detailed_experience.html', {'details':details, 'person':person}, context)


def search_alumni(request, username):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['first_name', 'last_name','course'])
        found_entries = alumni.objects.filter(entry_query)
        user = User.objects.get(username=username)
        person = student.objects.get(user=user)
 
    return render(request, 'alumni/search_results.html', {'query_string': query_string, 'found_entries': found_entries,'person':person })
        
        


                        
        
