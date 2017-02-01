from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
        variables =  { 'form': form }
 
    return render(request, 'registration/register.html',variables)
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
        if request.method == 'POST':
            form = UserInformationForm(request.POST)
            form.save()
            return HttpResponseRedirect('/home/')
        else:
            form = UserInformationForm()
            variables =  { 'form': form, 'user': request.user }
 
        return render(request,'home.html',variables)
        #variables =  { 'form': form, 'user': request.user }
        #return render(request,'home.html',variables)
         
