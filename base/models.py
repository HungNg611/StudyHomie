from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return (self.name)


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)     #allow null in db
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank= True) #null is set to true, can be blank
    #participants = 
    update = models.DateTimeField(auto_now =True) #auto_now : everytimes runs update its gonna take a timestamp
    created = models.DateTimeField(auto_now_add=True) #auto_now_add : know when room created

    #This is used to put the newest room on top
    class Meta:
        ordering = ['-update', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)   #one (project) to many (reviews) relationship
    body = models.TextField()
    update = models.DateTimeField(auto_now =True) #auto_now : everytimes runs update its gonna take a timestamp
    created = models.DateTimeField(auto_now_add=True) #auto_now_add : know when room created
    
    def __str__(self):
        return self.body[0:100] # message limit