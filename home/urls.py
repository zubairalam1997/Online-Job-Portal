from django.urls import path
from . import views
from .views import (JobCreateView, filter_jobs,)

app_name='home'
urlpatterns = [
    
    # home page
    path('', views.home_page, name='home_page'),
    # test 
    path('test/', views.index, name='index'),
    
    # form to create new jobs
    path('add_job/', JobCreateView.as_view(), name='addJob'),
    
    # search for jobs based on location and position
    path('filter_jobs/', views.filter_jobs, name='filter_jobs'),
    
    # view jobs 
    path('view_jobs/', views.viewJobs, name='viewJobs'),
    
    # brief detail of a job
    path('job_detail/<int:pk>', views.jobDetail, name='jobDetail'),
    
    # applying for job
    path('apply_for_job/<int:pk>', views.apply_for_job, name="apply_for_job"),
    
    # history of jobs applied for
    path('job_applications/', views.application_view, name='application_view'),
    
    # detail view of applied job applications
    path('applied_jobdeatils_view/<int:pk>', views.applied_jobdeatils_view, name='applied_jobdeatils_view'),
    
    # list of candidate's appplications for a job
    path('candidates_applications/', views.recieve_candidates_applications, name="candidates_applications_view"),
    
    # update job applications status for both candidate and employer
    path('update_status/<int:pk>', views.update_status, name='update_status'),
    
    # view resume of candidates applied for the job
    path('media/<int:pk>', views.open_resume, name='open_resume')
    
    # path('update_status/<int:pk>', views.update_status_reject, name='update_status_reject'),
    
    # path('saved_jobs<int:pk>/', views.save_jobs, name='savedJobs'),
    
]
