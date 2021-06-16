from django.db import models

# Create your models here.

class TaskUser(models.Model):
    user_name= models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    isadmin = models.BooleanField(default=False)
    name = models.CharField(max_length=20)

class Task(models.Model):
    title = models.CharField(max_length=20)
    details = models.TextField()
    date = models.DateField()
    tasks = models.ForeignKey(TaskUser,on_delete=models.CASCADE)

class Attachement(models.Model):
    title = models.CharField(max_length=20)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)

    