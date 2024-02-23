from django.db import models

# Create your models here.
class HospitalDetail(models.Model):
    
    hospital_name = models.CharField(max_length =200,blank=True,default=None)
    about_us = models.TextField(blank=True,default=None)
    learn_more = models.TextField(blank=True,default=None)
    specialization = models.TextField(blank=True,default=None)
    email_address = models.EmailField(blank=True,default=None)
    contact_number = models.IntegerField(blank=True,default=None)
    contact_address = models.TextField(blank=True,default=None)
    opening_hours = models.TextField(blank=True,default=None)
    hospital_rooms = models.IntegerField(blank=True,default=None)
    established_on = models.DateField(blank=True,default=None)
    promotions = models.TextField(blank=True,default=None)
    
    
    def __str__(self):
        return self.hospital_name
    
class ServiceDetail(models.Model):
    
    service_name = models.CharField(max_length=100,default=None,blank=True)
    description = models.TextField(blank=True, default=None)
    fee = models.IntegerField(blank=True,default=None)
    
class DoctorsDetail(models.Model):
    
    doctor_name=  models.CharField(max_length=100,default=None,blank=True)
    qualification = models.CharField(max_length=100,default=None,blank=True)
    specialization = models.CharField(max_length=100,default=None,blank=True)
    available_timings = models.TextField(default=None,blank=True)