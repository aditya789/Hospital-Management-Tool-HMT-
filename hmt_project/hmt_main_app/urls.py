from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_page, name='home'),
    path('contact',views.contact_page,name='contact')
]
