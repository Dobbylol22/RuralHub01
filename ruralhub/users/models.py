from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
# this class is for core authentication
class CustomUser(AbstractUser):
    #this field could store the OAuth provider's unique identifier for the user
    oauth_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    #optionally store the access token if needed for future API calls
    access_token = models.TextField(null=True, blank=True)
    #this field is to access the token
    email = models.EmailField(unique=True, null=False, blank=False)

#this class is just to store basic information of a particular user. 
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
