from django.db import models
from .utils import get_defaults
from django.db.models.signals import pre_save
from django.dispatch import receiver
defaults = get_defaults()

# Create your models here.
class HomePage(models.Model):

    hospital_name = models.CharField(
        max_length=200, blank=False, default=defaults.get('HospitalName'))
    contact_number = models.IntegerField(
        blank=True, default=defaults.get('ContactNumber'))
    headliner_1 = models.CharField(
        max_length=200, blank=False, default=defaults.get('Header'))
    headline_1_tagline = models.CharField(
        max_length=200, blank=False, default=defaults.get('HeaderTagline'))
    headliner_2 = models.CharField(
        max_length=200, blank=False, default=defaults.get('Header'))
    headline_2_tagline = models.CharField(
        max_length=200, blank=False, default=defaults.get('HeaderTagline'))
    headliner_3 = models.CharField(
        max_length=200, blank=False, default=defaults.get('Header'))
    headline_3_tagline = models.CharField(
        max_length=200, blank=False, default=defaults.get('HeaderTagline'))

    scheduler_1 = models.CharField(
        max_length=200, blank=False, default=defaults.get('Scheduler_1'))
    scheduler_1_tagline = models.TextField(
        blank=False, default=defaults.get('Scheduler_1_Tagline'))
    scheduler_2 = models.CharField(
        max_length=200, blank=False, default=defaults.get('Scheduler_2'))
    scheduler_2_tagline = models.TextField(
        blank=False, default=defaults.get('Scheduler_2_Tagline'))
    scheduler_3 = models.CharField(
        max_length=200, blank=False, default=defaults.get('Scheduler_3'))
    scheduler_3_tagline = models.TextField(blank=False,
                                           default=defaults.get('Scheduler_3_Tagline'))

    emergency_call_header = models.TextField(blank=False,
                                             default=defaults.get(
                                                 'EmergencyCallHeader')
                                             )
    emergency_call_tagline = models.TextField(blank=False,
                                              default=defaults.get('EmergencyCallTagline'))

    cleanliness_header = models.TextField(blank=False,
                                          default=defaults.get('CleanlinessHeader'))

    cleanliness_tagline = models.TextField(blank=False,
                                           default=defaults.get('CleanlinessTagline'))

    def __str__(self):
        return self.hospital_name
    
# will delete all the instances before new record was inserted
@receiver(pre_save, sender=HomePage)
def pre_save_homepage(sender, instance, **kwargs):
    HomePage.objects.all().delete()
