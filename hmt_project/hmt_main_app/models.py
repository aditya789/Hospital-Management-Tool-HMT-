from django.db import models

# Create your models here.
class HospitalDetail(models.Model):
    
    hospital_name = models.CharField(max_length =200,blank=True,default=None)
    
    
    
    def __str__(self):
        return self.hospital_name