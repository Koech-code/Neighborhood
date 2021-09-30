from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
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


    def __str__(self):
        return f'{self.name} Neighborhood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=50, blank=True, null=True)
    bio=models.TextField(max_length=500, null=True, blank=True)
    profile_pic=models.ImageField(upload_to='images', default='nopicture.png')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    
    def __str__(self):
        return f'{self.name} '

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Business(models.Model):
    name=models.CharField(max_length=40)
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    neighborhood_id=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email=models.EmailField()
    business_pic=models.ImageField(upload_to='images', default='nopicture.png')
    
    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

        
    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()


class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE )
    title=models.CharField(max_length=30)
    post=models.TextField(max_length=2000)
    date=models.DateTimeField(auto_now_add=True)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
