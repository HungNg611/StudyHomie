from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return (self.name)


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.SET_NULL, null=True)  # allow null in db
    name = models.CharField(max_length=200)
    # null is set to true, can be blank
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    # auto_now : everytimes runs update its gonna take a timestamp
    update = models.DateTimeField(auto_now=True)
    # auto_now_add : know when room created
    created = models.DateTimeField(auto_now_add=True)

    # This is used to put the newest room on top
    class Meta:
        ordering = ['-update', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # one (project) to many (reviews) relationship
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    # auto_now : everytimes runs update its gonna take a timestamp
    update = models.DateTimeField(auto_now=True)
    # auto_now_add : know when room created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:100]  # message limit
