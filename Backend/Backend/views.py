from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf

#User login method
def user_login(request):

    # If the request is a HTTP POST, pull the information required
    if request.method == 'POST':
        # Take in the username and password given by the user in the loginform.
        username = request.POST.get('username')
        password = request.POST.get('password')

        #If the username and password is correct - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If there isnt a user object then the details are wrong
        if user:
            # Is the account active? It may be disabled
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # Sends the user to the homepage
                login(request, user)
                return HttpResponseRedirect('/student/(?P<username>[a-zA-Z0-9]+)$/')
            else:
                # An inactive account was used - The user cannot login
                return HttpResponse("Your Student account is disabled.")
        else:
            # Incorrect login details were given by the user so the user cannot login
            return HttpResponse("Invalid login details supplied.")

    # Display the login form.
    # This scenario would most likely be a HTTP GET
    else:
        return render(request, 'login.html', {})

# Authorises the user login details    
def auth_view(request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
                auth.login(request, user)
                return redirect('student.views.index', username=username)
        else:
                return HttpResponseRedirect('/accounts/invalid')

#If the user is logged in
def loggedin(request):
        return render_to_response('loggedin.html',{'first_name': request.user.username})

#There is an invalid login
def invalid_login(request):
        return render_to_response('invalid_login.html')

#User logs out
def logout(request):
        auth.logout(request)
        return render_to_response('logout.html')
