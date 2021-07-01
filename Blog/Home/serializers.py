from rest_framework import serializers
from .models import Post,Feedback,Staff

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
        model=Feedback
        fields='__all__'              