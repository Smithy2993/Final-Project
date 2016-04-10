#Alumni views.py

#Import shortcuts, rendering and Httpresponse for the template purposes
#Also import the alumni forms from forms.py
#Also csrf for security purposes
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext
from alumni.forms import Find_AlumniForm
from django.db.models import Q
from django.core.context_processors import csrf

        
def alumni_search(request, form_class=Find_AlumniForm, template_name='alumni/Find_Alumni.html'):
        form = None
        if request.method == 'POST':
                #do search
                form = form_class(request.POST)
                if form.is_valid():
                        results = search(form.cleaned_data)
                        if results:
                                return render(request, template_name, {'form': form, 'Alumni': results})
        else:
                form = form_class()
        return render(request, template_name, {'form': form})

def search(search_data):
        q = Q()
        results = None
        searcher = alumni_search(search_data)
        
        for key in search_data.iterkeys():
                dispatch = getattr(searcher, 'search_%s' % key)
                q = dispatch(q)
        if q and len(q):
                results = alumni.objects.filter(q).select_related()
        #.order_by('-pk')
        else:
                results = []
        return results

class AlumniSearch(object):
        dictionary = []
        def __init__(self, search_data):
                self.dictionary.update(search_data)
        
        def search_keywords(self, q):
                if self.keywords:
                        words = self.keywords.split()
                        first_name_q = Q()
                        last_name_q = Q()
                        for word in words:
                                first_name_q = first_name_q | Q(first_name__icontains=word)
                                last_name_q = last_name_q | Q(last_name__icontains=word)
                        keyword_q = first_name_q | last_name_q
                        q = q & keyword_q
                return q
                                
                        
        
