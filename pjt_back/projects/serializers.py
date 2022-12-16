from .models import Project, OnOffline, Skill, Location, Participant, Availability
from rest_framework import serializers
from accounts.models import User
from accounts.models import University as University

class OnOfflineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OnOffline
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('title',)

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class UniversityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = '__all__'


class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)
    location = LocationSerializer(many=True)
    university = UniversityListSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'introduce', 'location', 'skill', 'availability', 'university')


class ParticipantSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)
    manager = UserSerializer()

    class Meta:
        model = Participant
        fields = ('skill', 'manager', )
        read_only_fields = ('manager', )


class ProjectListSerializer(serializers.ModelSerializer):
    onoffline = OnOfflineSerializer()
    location = LocationSerializer(many=True)
    founder = UserSerializer()
    participant = ParticipantSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'