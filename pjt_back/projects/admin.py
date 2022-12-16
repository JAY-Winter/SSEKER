from django.contrib import admin

from .models import Skill,Project, Location, OnOffline, Participant, Availability

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Location)
admin.site.register(OnOffline)
admin.site.register(Participant)
admin.site.register(Availability)