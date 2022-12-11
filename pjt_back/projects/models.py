from django.db import models
from django.conf import settings

class Location(models.Model):
    city = models.CharField(max_length=255)


class Skill(models.Model):
    title = models.CharField(max_length=255)


class OnOffline(models.Model):
    mode = models.IntegerField()
    title = models.TextField()


class Availability(models.Model):
    day = models.TextField()


class Project(models.Model):
    founder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='founder')
    participant = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    need_skill = models.ManyToManyField(Skill)
    onoffline = models.ForeignKey(OnOffline, on_delete=models.CASCADE)
    availability = models.ManyToManyField(Availability)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.ManyToManyField(Location)