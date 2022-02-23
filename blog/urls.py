from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import addblog,home_screen_view,detail_blog_view

urlpatterns = [
    path('post/', addblog,name="addblog"),
    path('allblog/',home_screen_view,name="allblog"),
    path('allblog/<pk>', detail_blog_view, name="detailblog"),
] 