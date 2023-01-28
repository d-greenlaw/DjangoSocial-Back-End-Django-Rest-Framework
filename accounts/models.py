from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    # profile_photo = models.ImageField(default='profile-default.png', upload_to='profile-images')
    # header_photo = models.ImageField(default='header-default.png', upload_to='header-images')
    # handle = models.CharField(max_length=50, blank=False)
    # email = models.EmailField(max_length=254, unique=True)
    # password = models.CharField(max_length=200)
    # bio = models.TextField(default="No bio yet!", max_length=300)
    # country = models.CharField(max_length=200, blank=True)
    # birth_day = models.DateTimeField(auto_now_add=False)
    # # Who sees my posts
    # following_me = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followingMe')
    # # Who's posts I see
    # im_following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='imFollowing')
    # # My friends regardless of who sees who's posts
    # friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='myFriends')
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email