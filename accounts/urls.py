from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('login/', views.log_in, name='log_in'),
    path('candidate_register/', views.candidate_sign_up, name='candidate_sign_up'),
    path('employer_register/', views.employer_sign_up, name='employer_sign_up'),
    path("logout/", views.Log_Out, name="logout"),
]
