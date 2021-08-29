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
        fields = '__all__'
class TaskSerializer(serializers.ModelSerializer):
    attachments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    creator = TaskUserSerializer(many=False,required=False)
    #assignee = TaskUserSerializer(many=False,read_only=True)
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Task
        fields = '__all__'
       
class UserSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(read_only=True,many=True) #serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    class Meta:
        model = User
        fields="__all__"


