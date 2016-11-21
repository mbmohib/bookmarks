from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=300, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images",)

    def __str__(self):
        return self.user.username
