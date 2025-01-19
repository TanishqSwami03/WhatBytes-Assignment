from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=now)
    last_updated = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        
        if self.pk:
            original_user = CustomUser.objects.get(pk=self.pk)
            if original_user.password != self.password:
                self.last_updated = now()

        super().save(*args, **kwargs)   