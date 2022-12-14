from .models import Campus, BaekJoonLevel, SkillCategory, Skill, Language, Track
from .serializers import CampusSerializer, TrackSerializer, BaekJoonLevelSerializer, SkillCategorySerializer, SkillSerializer, LanguageSerializer, LanguageCategorysSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def objects(request):
    skill          = SkillSerializer(Skill.objects.all(), many=True)
    track          = TrackSerializer(Track.objects.all(), many=True)
    campus         = CampusSerializer(Campus.objects.all(), many=True)
    language       = LanguageSerializer(Language.objects.all(), many=True)
    baekjoonlevel  = BaekJoonLevelSerializer(BaekJoonLevel.objects.all(), many=True)
    skill_category = SkillCategorySerializer(SkillCategory.objects.all(), many=True)
    
    context = { 
        'skill'         : skill.data,
        'track'         : track.data,
        'campus'        : campus.data,
        'language'      : language.data,
        'baekjoonlevel' : baekjoonlevel.data,
        'skill_category': skill_category.data,
    }
    return Response(context)

@api_view(['GET'])
def get_skill_language(request):
    skills = SkillSerializer(Skill.objects.all(), many=True).data
    languages = LanguageCategorysSerializer(Language.objects.all(), many=True).data
    context = [*skills, *languages]
    return Response(context)