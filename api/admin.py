from django.contrib import admin
from .models import TaskUser,Task,Attachement

# Register your models here.
admin.site.register(TaskUser)
admin.site.register(Task)
admin.site.register(Attachement)
