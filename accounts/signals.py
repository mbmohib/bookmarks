from django.db.models.signals import post_save

from django.dispatch import receiver
from django.contrib.auth.models import User
from posts.models import Category, UrlPost

from django.utils import timezone


@receiver(post_save, sender=User)
def add_new_user_data(sender, created, instance, **kwargs):
    if created:
        title_list = ['Social Site', 'Email', 'Newspaper', 'Shopping']
        for item in title_list:
            Category.objects.create(user=instance,
                                    title=item,
                                    created=timezone.now(),
                                    updated=timezone.now()
                                    )
        categories = Category.objects.filter(user=instance)
        url = [
            {
                'facebook': 'https://www.facebook.com',
                'twitter': 'https://www.twitter.com',
                'instagram': 'https://www.instagram.com'
            },
            {
                'gmail': 'https://gmail.com',
                'yahoo': 'https://mail.yahoo.com',
                'hotmail': 'https://account.live.com'},
            {
                'CNN': 'http://edition.cnn.com/',
                'BBC': 'http://www.bbc.com/news',
                'Al Jazeera': 'http://www.aljazeera.com/'},
            {
                'amazon': 'https://www.amazon.com',
                'ebay': 'https://www.ebay.com',
                'alibaba': 'https://www.alibaba.com/'
            }
        ]
        count = 0
        for category in categories:
            for key, value in url[count].items():
                UrlPost.objects.create(
                                        user=instance,
                                        category=category,
                                        title=key,
                                        url=value,
                                        status='public',
                                        created=timezone.now(),
                                        updated=timezone.now()
                )
            count += 1
