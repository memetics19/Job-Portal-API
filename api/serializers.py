from rest_framework import serializers
from .models import application,candidate

class applicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = application
        fields = "__all__"
        read_only_fields = ('id',)

class candidateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = candidate
        fields = "__all__"
        read_only_fields = ('id',)