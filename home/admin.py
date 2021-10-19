from django.contrib import admin
from .models import *

# Register your models here.
class job(admin.ModelAdmin):
    list_display = ('id','position', 'company', 'job_type','start_date','package','apply_by')
admin.site.register(Job, job)

class resume(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'mobile')
admin.site.register(Resume,resume)

class application(admin.ModelAdmin):
    list_display = ('id','position', 'company', 'job_type','start_date','package','apply_by',)
admin.site.register(Apply_for_job,application)

class job_applications(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'mobile', 'email',)
admin.site.register(Recieve_job_applications,job_applications)
