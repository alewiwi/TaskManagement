from rest_framework import serializers
from .models import Task,TaskUser,Attachement

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskUserSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = TaskUser
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True)
    class Meta:
        model = Attachement
        fields = '__all__'
