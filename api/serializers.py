from rest_framework import serializers
from .models import Task,Attachement
from django.contrib.auth.models import User


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachement
        fields = '__all__'

class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class TaskSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True)
    creator = TaskUserSerializer(many=False)
    assignee = TaskUserSerializer(many=False)
    class Meta:
        model = Task
        fields = '__all__'
       
class UserSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(read_only=True,many=True) #serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    class Meta:
        model = User
        fields="__all__"


