from rest_framework import serializers

from .models import Experience, Task



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['note']

class ExperienceSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = '__all__'
