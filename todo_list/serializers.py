from rest_framework import serializers
from .models import User, Todo, Categories, Events


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'description', 'completed', 'created_at', 'due_by', 'category', 'priority']

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'usesr_id']

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'name', 'start', 'end', 'status', 'created_by']