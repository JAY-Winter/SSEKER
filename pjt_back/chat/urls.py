from . import views
from django.urls import path

urlpatterns = [
    path('index', views.rocket_index),
    path('signup', views.rocket_signup),
    path('direct-room', views.direct_room),
]