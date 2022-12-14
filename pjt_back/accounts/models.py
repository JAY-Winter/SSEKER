from objects.models import Campus, Track, Skill, BaekJoonLevel, Language, Track, SkillCategory

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=True)
    campus = models.ForeignKey(Campus, blank=True, null=True, on_delete=models.CASCADE)
    part = models.IntegerField(default=0)
    skill = models.ManyToManyField(Skill, blank=True)
    github = models.CharField(max_length=300, blank=True, null=True)
    blog = models.CharField(max_length=300, blank=True, null=True)
    level = models.ForeignKey(BaekJoonLevel, blank=True, null=True, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, blank=True, null=True, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language, blank=True)
    introduce = models.CharField(max_length=2000, blank=True, null=True) 
    position = models.ForeignKey(SkillCategory, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50, blank=True, null=True) 
    generation = models.IntegerField(default=9)