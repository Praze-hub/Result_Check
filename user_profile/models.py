from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    level=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    def __str__(self):
        return f"{self.user.username}"


