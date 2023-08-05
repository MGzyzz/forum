from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='User'
    )

    avatar = models.ImageField(null=False, blank=False, upload_to='avatars', verbose_name='Avatar', default='default_avatars_user.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
