from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'backend/dashboard.html')

def dashboard_login(request):

    if request.user.is_authenticated:
        return redirect('/backend')

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #human = True
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/dashboard')
            else:
                messages.error(request, "Error: Wrong login or password")

    else:
        form = LoginForm()

    return render(request, 'backend/login.html',{'form': form})

def dashboard_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')
