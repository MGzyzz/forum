from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Theme(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='User')

    title = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='Summary'
    )
    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name='Description'
    )

    time_of_create = models.DateField(
        auto_now_add=True,
        verbose_name='Time of Creation'
    )
    count_answer = models.PositiveIntegerField(default=0)



    def __str__(self):
        return f'{self.user} created {self.title}'