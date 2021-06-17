from django.db import models

# Create your models here.

class TaskUser(models.Model):
    user_name= models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    isadmin = models.BooleanField(default=False)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=20)
    details = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(TaskUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Attachement(models.Model):
    title = models.CharField(max_length=20)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    