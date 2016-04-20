#Alumni views.py

#Import shortcuts, rendering and Httpresponse for the template purposes
#Also import the alumni forms from forms.py
#Also csrf for security purposes
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext
from alumni.models import alumni
from django.template.context_processors import csrf
import operator
from django.db.models import Q

def show_alumni(request):
        alumni_records = alumni.objects.all()
        all_alumni = {"alumni_detail" : alumni_records}
        print (all_alumni)
        return render_to_response('alumni/Find_Alumni.html', all_alumni, context_instance=RequestContext(request))
        
class find_alumni(alumni):
    paginate_by = 10

    def get_queryset(self):
        result = super(find_alumni, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(first_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(lastname_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(course__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(faculty__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(sector__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(self_employed__icontains=q) for q in query_list))
            )
        return result

                        
        
