from django.shortcuts import render
from django.http import HttpResponse
from extra_curricular.forms import extra_curricularForm

def index(request):
        context_dict = {'boldmessage' : "I am bold font from the context"}
        
        return render(request, 'extra_curricular/index.html', context_dict)

def add_extra_curricular(request):
        context = RequestContext(request)
        
        if request.method == 'POST':
                form = extra_curricularForm(request.POST)
                
                if form.is_valid():
                        form.save(commit=True)
                        return index(request)
                        
                else:
                        print (form.errors)

        else:
                form = extra_curricularForm()
                
        return render_to_response('extra_curricular/add_experience.html', {'form': form}, context)
                        
                        
                 
