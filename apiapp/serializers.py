from rest_framework import serializers
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'name',
            'short_description',
            'description',
            'goal',
            'amountRaised',
            'created',
            'updated',
            'finish',
            'creator',
            'category',
        )
