from rest_framework import serializers
from .models import CustomUser, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'avatar', 'level', 'rank', 'balance']

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'category', 'reward', 'tags', 'created_at']
        read_only_fields = ['id', 'created_at', 'user']
