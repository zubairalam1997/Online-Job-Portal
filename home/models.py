from typing import Match
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Job(models.Model):
    jobType = (('','Choose job-type:'),
               ('Internship','Internship'),
               ('Part-Time','Part-Time'),
               ('Full-time','Full-time'),
    )
    position = models.CharField(max_length=200, null=False)
    company = models.CharField(max_length=200, null=False)
    start_date = models.CharField(max_length=200, null=False)
    job_type = models.CharField(max_length=50, null=False, choices=jobType)
    package = models.CharField(max_length=200, null=False)
    apply_by = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=200, null=True)
    about_company = models.TextField(max_length=1500, null=False)
    job_description = models.TextField(max_length=1500, null=False)
    eligibility = models.TextField(max_length=500, null=False)
    perks = models.TextField(max_length=500, null=False)
    openings = models.IntegerField( null=False)
    # is_applied = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.position
    
    def get_absolute_url(self):
        return reverse("home:jobDetail", kwargs={"pk": self.pk})

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200 , null=False)
    last_name = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=13, null=False, default="+91")
    resume = models.FileField( upload_to='resume/', null=True)
    address = models.CharField(max_length=300, null=True)
    
class Apply_for_job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE) #error
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, null=False)
    company = models.CharField(max_length=200, null=False)
    start_date = models.CharField(max_length=200, null=False)
    job_type = models.CharField(max_length=50, null=False)
    package = models.CharField(max_length=200, null=False)
    apply_by = models.CharField(max_length=200, null=False)
    applied_by = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    
    # def __str__(self):
    #     return self.job.position
    
    def get_absolute_url(self):
        return reverse("home:application_view", kwargs={"pk": self.pk})

    
    
class Recieve_job_applications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    apply_for_job = models.ForeignKey(Apply_for_job, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200 ,null=False)
    position = models.CharField(max_length=200, null=True)
    applied_by = models.CharField(max_length=200, null=True)
    resume_file = models.FileField(null=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    job_created_by = models.CharField(max_length=200, null=True)
    
    def get_absolute_url(self):
        return reverse("home:candidates_applications_view", kwargs={"pk": self.pk})
    
    def get_resume_url(self):
        return reverse("home:open_resume", kwargs={'pk':self.pk})
    
    
# class Create_resume(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # personal information
#     name = models.CharField(max_length=50, null=False)
#     email = models.EmailField(null=False)
#     phone_number = models.CharField(max_length=13, null=False)
#     address = models.CharField(max_length=300, null=False)
#     # qualifications
#         # graduation
#     university_name = models.CharField(max_length=100, null=False)
#     university_location = models.CharField(max_length=200, null=False)
#     degree = models.CharField(max_length=100, null=False)
#     branch = models.CharField(max_length=200, null=False)
#     degree_duration = models.DurationField(null=False)
#         # high school
#     school_name = models.CharField(max_length=200, null=False)
#     school_location = models.CharField(max_length=200, null=False)
#     class_name = models.CharField(max_length=200, null=False)
#     branch = models.CharField(max_length=200, null=False)
#     class_duration = models.DurationField(null=False)
#     # Certifications
    
    
    
# class Employer(models.Model):
#     user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
#     name=models.CharField(max_length=200,null=True)
#     position=models.CharField(max_length=200,null=True)
#     description=models.CharField(max_length=2000,null=True)
#     salary=models.IntegerField(null=True)
#     experience=models.IntegerField(null=True)
#     Location=models.CharField(max_length=2000,null=True)
#     profile = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name
    
# class Candidate(models.Model):
#     category=(
#         ('Male','male'),
#         ('Female','female'),
#         ('Other','other'),
#     )
#     name=models.CharField(max_length=200,null=True)
#     dob=models.DateField(null=True)
#     gender= models.CharField(max_length=200,null=True,choices=category)
#     mobile= models.CharField(max_length=200,null=True)
#     email= models.CharField(max_length=200,null=True)
#     resume=models.FileField(null=True)
#     company=models.ManyToManyField(Employer,blank=True)
#     profile = models.CharField(max_length=200, default="Candidate")
#     def __str__(self):
#         return self.name
