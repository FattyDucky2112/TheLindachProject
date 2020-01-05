from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    lastname = models.CharField(blank = True, max_length = 20)
    firstname = models.CharField(blank = True, max_length = 20)
    def __str__(self):
        return self.user.username
