import os
from django.db import models
from django.http import request
from django.http import response
from django.http.response import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from django.contrib import messages
from home.admin import resume
# from django.contrib.auth.mixins import LoginRequiredMixin

from home.models import Apply_for_job, Job, Recieve_job_applications, Resume

# Create your views here.
def home_page(request): 
    jobs_feed = Job.objects.all()      
    user = request.user
    context = {
        'user':user,
        'jobs':jobs_feed
    } 
    return render(request, 'home/home.html', context)

def index(request):
    job = Job.objects.all()
    userr = request.POST.get('first_name')
    user = request.user
    # recieve = Recieve_job_applications.objects.get()
    context = {
        'job':job,
        'userr':userr,
        'user':user
    }
    
    return render(request, 'home/test.html', context)


class JobCreateView(CreateView):
    model = Job
    fields = ['position', 'company', 'job_type', 'start_date', 'package', 'apply_by', 'location', 'about_company', 'job_description', 'eligibility', 'perks', 'openings', 'created_by']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
def filter_jobs(request):
    position = request.POST.get('position')
    location = request.POST.get('location')
    job = Job.objects.filter(position=position, location=location)
    return render(request, 'home/home.html', {'jobs':job})

def viewJobs(request):
    job = Job.objects.filter(created_by=request.user)
    return render(request, 'home/jobs.html', {'job':job})
    
def jobDetail(request, pk):
    job = Job.objects.get(pk=pk)
    # applied = getattr(job, 'is_applied')
    id = pk
    context={
        'job':job,
        'id':id,
    }
    return render(request, 'home/job_detail.html', context)

def apply_for_job(request, pk):
    user = request.user
    resume = Resume.objects.get(user=user)
    job = get_object_or_404(Job, pk=pk)
    jobb = Job.objects.filter(pk=pk)
    position = getattr(job,'position')
    company = getattr(job,"company")
    start_date = getattr(job,"start_date")
    package = getattr(job,"package")
    apply_by = getattr(job,"apply_by")
    job_type = getattr(job,"job_type")
    job_created_by = getattr(job, 'created_by')
    applied_by = request.user 
    mobile = getattr(resume, 'mobile')
    first_name = getattr(user, "first_name")
    last_name = getattr(user, 'last_name')
    email = getattr(user, 'email')
    resumee = getattr(resume, 'resume')
    
    apply_for_job = Apply_for_job.objects.create(user=request.user, job=job, resume=resume, position= position, company=company, start_date=start_date, package=package, apply_by=apply_by, job_type=job_type, applied_by=applied_by)
    Recieve_job_applications.objects.create(user=request.user, job=job, resume=resume, resume_file=resumee, apply_for_job=apply_for_job, first_name=first_name, last_name=last_name, email=email, mobile=mobile, position=position, applied_by=applied_by, job_created_by=job_created_by)
    return redirect('home:home_page')

def application_view(request):    
    jobs = Apply_for_job.objects.filter(user = request.user)
    return render(request, 'home/applications.html', {'jobs':jobs})

def applied_jobdeatils_view(request, pk):
    job = Job.objects.get(pk=pk)
    return render(request, 'home/applied_job_detail.html', {'job':job})

def recieve_candidates_applications(request):
    recieve = Recieve_job_applications.objects.filter(job_created_by=request.user)
    return render(request, 'home/recieve_applications.html', {'recieve': recieve})

def update_status(request, pk):
    recieve = Recieve_job_applications.objects.filter(pk=pk)
    recievee = Recieve_job_applications.objects.get(pk=pk) #help .get for getattr() and .filter for update()
    applied_by = getattr(recievee, "applied_by")
    apply = Apply_for_job.objects.filter(applied_by=applied_by)
    if request.method == 'POST':
        status = request.POST['status']
        if status=='Hire':
            recieve.update(status="Hired!")
            apply.update(status="Hired!")
        else:
            recieve.update(status="Rejected!")
            apply.update(status="Rejected!")

    return redirect("home:candidates_applications_view")


def open_resume(request, pk):
    recieve = Recieve_job_applications.objects.get(pk = pk)
    resume = getattr(recieve, 'resume_file')
    response = redirect(f'{resume}')
    return response

