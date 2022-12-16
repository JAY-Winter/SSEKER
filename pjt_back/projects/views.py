from .models import Project, OnOffline, Skill, Availability, Location, Participant
from .serializers import ProjectListSerializer, OnOfflineSerializer, SkillSerializer, AvailabilitySerializer, LocationSerializer, ProjectSerializer

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from datetime import datetime
from django.utils import timezone           


@api_view(['GET'])
def projects(request, project_id=None):
    if request.method == 'GET':
        if project_id:
            project = get_object_or_404(Project, id=project_id)
            serializer = ProjectListSerializer(project)
        else:
            projects = Project.objects.all()
            serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def project_detail(request):
    if request.method == 'POST':
        onoffline = OnOffline.objects.get(id=request.data['onoffline'])
        location = Location.objects.get(id=request.data['selectedLocation'])

        start_date = list(map(int, (request.data['selectedDates'][0]).split('-')))
        end_date = list(map(int, (request.data['selectedDates'][1]).split('-'))) 

        start_date = datetime(start_date[0], start_date[1], start_date[2])
        end_date = datetime(end_date[0], end_date[1], end_date[2])

        project = Project.objects.create(
            founder = request.user,
            title = request.data['title'],
            content = request.data['content'],
            onoffline = onoffline,
            start_date = start_date,
            end_date = end_date,
        )
        project.save()

        for par in request.data['selectedParticipant']:
            sel_skill = par['selectedSkill']
            skill = Skill.objects.get(title=sel_skill)
            participant = Participant.objects.create()
            participant.save()
            participant.skill.add(skill)
            project.participant.add(participant)
            
        project.location.add(location)  

        for ava in list(map(int,(request.data['selectedAvailability']))):
            availability = Availability.objects.get(id=ava)
            project.availability.add(availability)


        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def adprojects(request):
    if request.method == 'GET':
        projects = Project.objects.order_by('?')[:3]
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def objects(request):
    if request.method == 'GET':
        skill = Skill.objects.all()
        location = Location.objects.all()
        onoffline = OnOffline.objects.all()
        availability = Availability.objects.all()

        skill_serializer = SkillSerializer(skill, many=True)
        location_serializer = LocationSerializer(location, many=True)
        onoffline_serializer = OnOfflineSerializer(onoffline, many=True)
        availability_serializer = AvailabilitySerializer(availability, many=True)
        
        context = {
            'onoffline': onoffline_serializer.data,
            'skill': skill_serializer.data,
            'availability': availability_serializer.data,
            'location': location_serializer.data,
        }
        return Response(context)

