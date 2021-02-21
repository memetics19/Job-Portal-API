from rest_framework import serializers
from .models import application,candidate
from accounts.models import UserProfile
    

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

class CandidateUserProfileSerializer(serializers.Serializer):
    class Meta:
        model =UserProfile
        fields = "__all__"
        read_only_fields = ('id',)

# class HrUserProfileSerializer(serializers.Serializer):
#     class Meta:
#         model = HrUserProfile
#         fields = "__all__"
#         read_only_fields = ('id',)