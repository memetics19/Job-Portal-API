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

class CandidateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','email','name','password')
        extra_kwargs  = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

        def create(self,validated_data):
            user = UserProfile.objects.create(
                email = validated_data['email'],
                name = validated_data['name'],
                password = validated_data['password']
            )
            return user

        def update(self, instance, validated_data):
            if 'password' in validated_data:
                password = validated_data.pop('password')
                instance.set_password(password)
 
            return super().update(instance, validated_data)