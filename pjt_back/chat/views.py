import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render
from rocketchat.api import RocketChatAPI

def rocket_index(request):
    return render(request, 'accounts/test.html')


@api_view(['POST'])
def rocket_signup(request):
    admin_token = 'dVSTCd0aihjwcqmlfRYWi25juWyI3F3CpilBJviRhYM'
    admin_user_id = 'MsxKCXtaxzoxJ3Km6'
    headers = {
        'X-Auth-Token': admin_token,
        'X-User-Id': admin_user_id,
    }

    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    username = request.data.get('username')

    json_data = {
        'name': name,
        'email': email,
        'password': password,
        'username': username,
    }

    response = requests.post('http://localhost:3000/api/v1/users.create', headers=headers, json=json_data)
    print(response.json())
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def direct_room(request):
    api = RocketChatAPI(settings={'token': 'dVSTCd0aihjwcqmlfRYWi25juWyI3F3CpilBJviRhYM', 'user_id': 'MsxKCXtaxzoxJ3Km6',
                                'domain': 'http://localhost:3000'})
    username = ''
    api.create_im_room(
        username=username,
)