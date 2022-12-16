from django.db import models
from django.contrib.auth.models import AbstractUser
from projects.models import Skill as Skill
from projects.models import OnOffline as OnOffline
from projects.models import Availability as Availability
from projects.models import Location as Location

class University(models.Model):
    name = models.CharField(max_length=255) 

class Interest(models.Model):
    name = models.CharField(max_length=255)

class User(AbstractUser):
    followings = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')
    location = models.ManyToManyField(Location, blank=True,)
    university = models.ForeignKey(University, blank=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=1000, blank=True)
    introduce = models.CharField(max_length=300, blank=True, null=True)
    skill = models.ManyToManyField(Skill, blank=True)
    availability = models.ManyToManyField(Availability, blank=True)
    onoffline = models.ForeignKey(OnOffline, blank=True, null=True, on_delete=models.CASCADE)
    interest = models.ManyToManyField(Interest, blank=True)