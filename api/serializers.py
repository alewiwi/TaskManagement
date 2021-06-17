from rest_framework import serializers
from .models import Task,TaskUser,Attachement


class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskUser
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True)
    class Meta:
        model = Attachement
        fields = '__all__'
