from rest_framework import serializers
from .models import BlogPost, BlogPostImage
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class BlogPostImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPostImage
        fields = ['id', 'image']

class BlogPostSerializer(serializers.ModelSerializer):
    images = BlogPostImageSerializers(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'description', 'content', 'created_at', 'views', 'images']