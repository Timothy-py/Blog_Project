from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    picture = models.ImageField(upload_to = "profile_pics", default = "software-developer-icon-png-2.png")

    def __str__(self):
        return f"{self.user.username}"
