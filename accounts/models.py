from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=300, blank=True)
    profile_pic = models.ImageField(
                null=True, blank=True, upload_to=user_directory_path)

    def __str__(self):
        return self.user.username
