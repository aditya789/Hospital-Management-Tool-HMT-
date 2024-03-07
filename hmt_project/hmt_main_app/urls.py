from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('',RedirectView.as_view(url='home/', permanent=False), name='index'), 
    path('doctors/', views.doctors_page ,name='doctors'),
    path('services/',views.services_page,name ='services'),
    path('highlights/',views.highlights_page,name='highlights'),
    path('contact/',views.contact_page,name='contact'),
    path('appointments/', views.appointments_page ,name='appointments')
]
