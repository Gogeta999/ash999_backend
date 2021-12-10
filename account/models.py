from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class User(AbstractUser):
    nickname = models.CharField(max_length=11)
    created_time = models.DateTimeField('Created Time', default=now)
    last_modified_time = models.DateTimeField('Last Modified', default=now)

    def __str__(self):
        return self.username