from django.urls import path,include
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/',UserList.as_view()),
    path('tasks/',TaskList.as_view()),
    path('users/<int:pk>/',UserDetails.as_view()),
    path('tasks/<int:pk>/',TaskDetails.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('login/',obtain_auth_token),
    path('upload/', FileUploadView.as_view()),
    path('login2/', CustomAuthToken.as_view()),
]