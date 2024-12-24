from rest_framework import serializers
from .models import CustomUser, Task


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'avatar', 'level', 'rank', 'balance']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    executor = UserSerializer(read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Task
        fields = ['id', 'user', 'executor', 'title', 'description', 'category', 'reward', 'tags', 'created_at', 'image']
        read_only_fields = ['id', 'created_at', 'user', 'executor']