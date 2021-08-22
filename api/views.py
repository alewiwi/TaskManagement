from django.shortcuts import render,HttpResponse
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,FileUploadParser
from rest_framework import authentication,permissions
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import generics

# Create your views here.

# @api_view(['GET'])
# def get_tasks_list(request):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TaskSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201,safe=False)
#         else:
#             return  JsonResponse(serializer.errors,status=400,safe=False)
# @api_view(['GET'])
# def get_task(request,task_id):
#     task = get_object_or_404(Task,id=task_id)
#     #task = Task.objects.get(id=task)
#     serializer = TaskSerializer(task)
#     return JsonResponse(serializer.data,safe=False)

# @api_view(['POST'])
# def create_task(request):
#     serializer = TaskSerializer(creator=request.user,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)

# @api_view(['POST'])
# def update_task(request,task_id):
#     task = get_object_or_404(Task,id=task_id)
#     serializer = TaskSerializer(instance=task,data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)

# @api_view(['DELETE'])
# def delete_task(request,task_id):
#     task = get_object_or_404(Task,id=task_id)
#     serializer = TaskSerializer(instance=task)

#     if serializer.is_valid():
#         serializer.delete()
#     return JsonResponse(serializer.data,safe=False)

# @api_view(['GET'])
# def get_users_list(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201,safe=False)
#         else:
#             return JsonResponse(serializer.errors,status=400,safe=False)

# @api_view(['GET'])
# def get_user(request,user_id):
#     user = get_object_or_404(User,id=user_id)
#     serializer = UserSerializer(user)
#     print(user)
#     return JsonResponse(serializer.data,safe=False)

# @api_view(['POST'])
# def create_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)

# @api_view(['POST'])
# def update_user(request,user_id):
#     user = get_object_or_404(User,id=user_id)
#     serializer = UserSerializer(instance=user,data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)

# @api_view(['DELETE'])
# def delete_user(request,user_id):
#     user = get_object_or_404(User,id=user_id)
#     serializer = TaskSerializer(instance=user)

#     if serializer.is_valid():
#         serializer.delete()
#     return JsonResponse(serializer.data,safe=False)
class UserList(generics.ListAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]
    def get(self,request,format=None):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)

        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskList(APIView):
    def get(self,request,format=None):
        user = self.request.user
        if(user.is_superuser):
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks,many=True)
            return Response(serializer.data)
        else:
            tasks = Task.objects.filter(assignee=user)
            serializer = TaskSerializer(tasks,many=True)
            return Response(serializer.data)
        

    def post(self,request,format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetails(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FileUploadView(APIView):
    parser_classes = [FileUploadParser]
    #authentication_classes=[authentication.TokenAuthentication]
    def get(self,request):
        pass
    
    def post(self,request):
        file_obj = request.data['file']
        return Response(status=204)

    def put(self,request):
        file_obj = request.data['file']
        return Response(status=204)