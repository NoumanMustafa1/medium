from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
# Create your models here.
current_time = timezone.now()


class USER(AbstractUser):
    class Role(models.TextChoices):
        READER = "READER",'Reader'
        VIEWER = "VIEWER",'Viewer'
    base_role = Role.READER
    role = models.CharField(max_length=50,choices=Role.choices)

    def save(self,*arg,**kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*arg, **kwargs)

# Create your models here.
class BlogModel(models.Model):
    img = models.ImageField(upload_to="images")
    reading_time = models.IntegerField(default=1)
    date = models.DateField(default=current_time)
    alt_img = models.ImageField(upload_to="images")
    title = models.CharField(max_length=200, default=None)
    author = models.CharField(max_length=1200, default=None)
    language = models.CharField(max_length=200, default=None)
    category = models.CharField(max_length=200, default=None)
    blog_link = models.CharField(max_length=200, default=None)
    description = models.CharField(max_length=800, default=None)
    audience_type = models.CharField(max_length=200, default=None)
    recommendation_type = models.CharField(max_length=200, default=None)

    def __str__(self) -> str:
        return self.title


class userModel(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    interests = models.CharField(max_length=200)
    preference = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200)
    is_reader = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

# class userPreferenceModel(models.Model):
#     pass
