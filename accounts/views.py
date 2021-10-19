from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from home.models import Resume
from .forms import Candidate_RegistrationForm, Employer_RegistrationForm
from . import models

# Create your views here.
def candidate_sign_up(request):
    if (request.method == 'POST'):
        form = Candidate_RegistrationForm(request.POST, request.FILES)
        if (form.is_valid()):
            user = form.save()
            
            # assigning groups
            group = Group.objects.get(name='Candidate')
            user.groups.add(group) 
                 
            #saving resume doc to resume model
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            mobile = request.POST.get("mobile")
            # resume = request.POST.get("resume")
            resume = request.FILES["resume"]
            address = request.POST.get('address')
            resume_obj = Resume(first_name=first_name, last_name=last_name, mobile=mobile, resume=resume, address=address)
            resume_obj.user = user
            resume_obj.save()
                         
            login(request, user)
            return redirect('home:home_page')
    else:
        form = Candidate_RegistrationForm()
    return render(request, 'accounts/register.html', { 'form': form })

def employer_sign_up(request):
    if (request.method == 'POST'):
        form = Employer_RegistrationForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            
            # assigning groups
            group = Group.objects.get(name='Employer')
            user.groups.add(group)
                         
            login(request, user)
            return redirect('home:home_page')
    else:
        form = Employer_RegistrationForm()
    return render(request, 'accounts/register.html', { 'form': form })

def log_in(request):
    if (request.method == 'POST'):
        form = AuthenticationForm(data=request.POST)
        if (form.is_valid()):
            user = form.get_user()
            login(request, user)
            return redirect('home:home_page')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def Log_Out(request):
    if (request.method == 'POST'):
        logout(request)
        return redirect('/')