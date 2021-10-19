from django.db import models
from django.db.models.base import Model
from home.models import User
from django.shortcuts import reverse

# Create your models here.
class Identity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # personal information
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=300, null=True)
    
    def get_absolute_url(self):
        return reverse("create_resume:resume", kwargs={"pk": self.pk})
    
    def get_update_identity_url(self):
        return reverse("create_resume:update-identity", kwargs={'pk': self.pk})
    
    
# Experience
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    duration = models.CharField(max_length=100, null=False)
    # ongoing = models.BooleanField(default=False)
    desc = models.TextField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("create_resume:resume", kwargs={})
    
    def get_delete_url(self):
        return reverse('create_resume:resume', kwargs={'pk':self.pk})

# Internship    
class Internship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name  = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    duration = models.CharField(null=False, max_length=100)
    # ongoing = models.BooleanField(default=False)
    location = models.CharField(max_length=200, null=True)
    desc = models.TextField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("create_resume:resume", kwargs={})

# Qulaifications

class Qualifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=200, null=True)
    degree = models.CharField(max_length=100, null=True)
    branch = models.CharField(max_length=200, null=True)
    duration = models.CharField(null=False, max_length=100)
    # ongoing = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("create_resume:resume", kwargs={})
    
    
    # def get_absolute_url(self):
    #     return reverse("create_resume:create-qualifications", kwargs={})
    

# class Masters(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     masters_university_name = models.CharField(max_length=100, null=True)
#     masters_university_location = models.CharField(max_length=200, null=True)
#     masters_degree = models.CharField(max_length=100, null=True)
#     masters_branch = models.CharField(max_length=200, null=True)
#     masters_degree_duration = models.DurationField()
#     master_pursuing = models.BooleanField(default=False)

# class Bachelors(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     bachelors_university_name = models.CharField(max_length=100, null=True)
#     bachelors_university_location = models.CharField(max_length=200, null=True)
#     bachelors_degree = models.CharField(max_length=100, null=True)
#     bachelors_branch = models.CharField(max_length=200, null=True)
#     bachelors_degree_duration = models.DurationField()
#     bachelors_pursuing = models.BooleanField(default=False)
    
# class High_school(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     school_name = models.CharField(max_length=200, null=True)
#     school_location = models.CharField(max_length=200, null=True)
#     class_name = models.CharField(max_length=200, null=True)
#     branch = models.CharField(max_length=200, null=True)
#     class_duration = models.DurationField()
    
# Certifications
class Certifications(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE) 
   name = models.CharField(max_length=200, null=True)
   company = models.CharField(max_length=200, null=True)
   duration = models.CharField(null=False, max_length=100)
   desc = models.TextField(null=True, blank=True)
   
   def get_absolute_url(self):
       return reverse("create_resume:resume", kwargs={})
   
    

# Projects
class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    duration = models.CharField(null=False, max_length=100)
    # ongoing = models.BooleanField(default=False)
    desc = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("create_resume:resume", kwargs={})
    
# skills
class Technical_skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=200, null=True)
    expertise = models.CharField(max_length=100, null=True)  
    
    def get_absolute_url(self):
        return reverse("create_resume:resume", kwargs={}) 
   
