from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_image', blank=True, null=True)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)
        if img.height > 100 or img.width > 100:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

class RequestTeacher(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    tel_number = models.CharField(max_length=15)

    def __str__(self):
        return self.profile.user.username
        