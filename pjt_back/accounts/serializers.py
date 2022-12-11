from rest_framework import serializers
from .models import User, Location, Interest
from projects.models import Availability as Availability
from projects.serializers import SkillSerializer as SkillSerializer
from projects.serializers import OnOfflineSerializer as OnOfflineSerializer
from projects.serializers import UniversityListSerializer as UniversityListSerializer

class AvailabilitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Availability
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = '__all__'

class UserListSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)
    availability = AvailabilitySerializer(many=True)
    onoffline = OnOfflineSerializer()
    location = LocationSerializer(many=True)
    university = UniversityListSerializer()
    interest = InterestSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'