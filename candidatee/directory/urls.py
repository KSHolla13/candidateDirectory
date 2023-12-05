from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('', CandidateDirectoryAV.as_view(), name='movie-list'),
    path('<int:pk>/',CandidateDirectoryDetailAV.as_view(), name='movie-detail'),
]

    