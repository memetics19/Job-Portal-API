from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import application,candidate
from .serializers import applicationSerializer, candidateSerializer
# Create your views here.


class applicationView(ModelViewSet):
    queryset = application.objects.all()
    serializer_class = applicationSerializer

class candidateView(ModelViewSet):
    queryset = candidate.objects.all()
    serializer_class = candidateSerializer