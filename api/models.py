from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=20)
    details = models.TextField()
    date = models.DateField()
    done = models.BooleanField(default=False)
    creator = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name="creator")
    assignee = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name="tasks") 

    def __str__(self):
        attachement = self.attachement_set
        return self.title

class Attachement(models.Model):
    title = models.CharField(max_length=20)
    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name="attachments")

    def __str__(self):
        return self.title
    