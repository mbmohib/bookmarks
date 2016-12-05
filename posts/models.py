from django.db import models

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(
            User, related_name='user_cat', on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    sub_cat = models.ForeignKey("self")

    class Meta:
        verbose_name_plural = 'category'

    def __str__(self):
        return self.title


class UrlPost(models.Model):
    STATUS_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    user = models.ForeignKey(
            User, related_name='user_post', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    status = models.CharField(
                max_length=10, choices=STATUS_CHOICES, default='public')
    note = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'url Post'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
