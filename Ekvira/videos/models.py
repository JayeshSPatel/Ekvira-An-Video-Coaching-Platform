from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to="videos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )  # Add this field


    def __str__(self):
        return self.title
