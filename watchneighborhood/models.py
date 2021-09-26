from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.


class Neighborhood(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    occupants=models.IntegerField()
    image=models.ImageField(upload_to='images', default='logo.png')
    admin=models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='hood')
    description = models.TextField(max_length=200)
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=50, blank=True, null=True)
    profile_pic=models.ImageField(upload_to='images', default='nopicture.png')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

class Business(models.Model):
    name=models.CharField(max_length=40)
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    neighborhood_id=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email=models.EmailField()

class Post(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE )
    title=models.CharField(max_length=30)
    post=models.TextField(max_length=2000)
    date=models.DateTimeField(auto_now_add=True)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
