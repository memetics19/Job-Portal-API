from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import application,candidate
from .serializers import applicationSerializer, candidateSerializer, CandidateUserProfileSerializer
from rest_framework import status
from accounts.models import UserProfile
import requests
import logging 



logger = logging.getLogger(__name__)

class applicationView(ModelViewSet):
    queryset = application.objects.all()
    serializer_class = applicationSerializer
    logger.info("Application for vacany successfully registered")


class candidateView(ModelViewSet):
    queryset = candidate.objects.all()
    serializer_class = candidateSerializer
    logger.info("Candidate successfully applied the job")

class CandidateUserProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = CandidateUserProfileSerializer

