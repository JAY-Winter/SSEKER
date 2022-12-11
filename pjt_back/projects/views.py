from .models import Project
from .serializers import ProjectListSerializer

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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

@api_view(['GET'])
def adprojects(request):
    if request.method == 'GET':
        projects = Project.objects.order_by('?')[:3]
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data)