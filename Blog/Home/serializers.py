from rest_framework import serializers
from .models import Post,Feedback,Staff
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'        
        
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields = ('id','username','password','name', 'email')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = Staff.objects.create_user(validated_data['username'],password = validated_data['password']  ,name=validated_data['name'],  email=validated_data['email'])
        return user
# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'             