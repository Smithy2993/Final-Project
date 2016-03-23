# extra_curricular views.py

# Import shortcuts modules aswell as the http responses
# Import the templates and the extra_curricular forms
# Import csrf for security purposes
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext
from extra_curricular.forms import extra_curricularForm
from django.core.context_processors import csrf

def index(request):
        context_dict = {'boldmessage' : "I am bold font from the context"}
        
        return render(request, 'extra_curricular/index.html', context_dict)

# Add extra_curricular method
def add_extra_curricular(request):
        
        if request.method == 'POST':
                form = extra_curricularForm(request.POST)
                
                if form.is_valid():
                        form.save(commit=True)
                        return index(request)
                        
                else:
                        print (form.errors)

        else:
                form = extra_curricularForm()
                
        return render_to_response('extra_curricular/add_experience.html', {'form': form}, RequestContext(request))
                        
                        
                 
