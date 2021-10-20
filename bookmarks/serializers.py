from rest_framework import serializers
from .models import Bookmark
from django.contrib.auth.models import User


class BookmarkSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Bookmark
        fields = ['title', 'url', 'user', 'created_at']