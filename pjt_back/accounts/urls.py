from . import views
from django.urls import path

urlpatterns = [
    path('', views.peoples),
    path('<str:username>', views.people_detail),
    path('user/search', views.search),
    path('user/recommend-users', views.recommend_users),
    path('rocketchat/index', views.rocket_index),
    path('rocketchat/api/signup', views.rocket_signup),
]