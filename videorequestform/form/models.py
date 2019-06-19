from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=20)
    video_desc=models.TextField()
    date=models.DateTimeField(default=timezone.now())

