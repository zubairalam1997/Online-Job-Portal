from django.urls import path
from . import views
from .views import (
    IdentityUpdateView,
    # create
    QualificationsCreateView,
    ExperienceCreateView,
    InternshipCreateView,
    CertificationsCreateView,
    ProjectsCreateView,
    Technical_skillsCreateView,
    # delete
    ExperienceDeleteView,
)

app_name = 'create_resume'
urlpatterns = [
    path('resume/',views.resume, name='resume'),
    path('identity-update/', IdentityUpdateView.as_view(), name='update-identity'),
    
    # create
    path('create-qualifications/', QualificationsCreateView.as_view(), name='create-qualifications' ),
    path('create-experience/', ExperienceCreateView.as_view(), name='create-experience' ),
    path('create-internship/', InternshipCreateView.as_view(), name='create-internship'),
    path('create-certification/', CertificationsCreateView.as_view(), name='create-certifications'),
    path('create-project/', ProjectsCreateView.as_view(), name='create-projects'),
    path('create-technical-skill/', Technical_skillsCreateView.as_view(), name='create-technical-skills'),
    
    #delete
    path('delete-experience/<int:pk>', ExperienceDeleteView.as_view(), name='delete-experience')
] 
