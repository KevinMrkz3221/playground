from rest_framework import serializers

from .models import Project, ProjectTag, ProjectImage, Technology


class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTag  
        fields = ['name']

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['image']

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)
    technologies = TechnologySerializer(many=True, read_only=True)
    images = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('title', 'description', 'github', 'web', 'images', 'technologies', 'tags')

    def get_image(self, obj):
        return obj.image.url