from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='user_follower_set', blank=True)
    following = models.ManyToManyField(
        "self",                 # self-referential: users follow other users
        symmetrical=False,      # following is not always mutual
        related_name="user_following_set",  # allows reverse lookup (who follows me)
        blank=True
    )

    def __str__(self):
        return self.username