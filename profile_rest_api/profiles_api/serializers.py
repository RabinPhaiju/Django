from dataclasses import field
from tkinter.tix import Tree
from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
        
    def create(self,validated_data):
        """"Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email= validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    
    
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on','updated_on','verified')
        extra_kwargs = {'user_profile':{'read_only':True}} # make user_profile read only