from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_countries.fields import CountryField
# Create your models here.

class Profile(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('Other', 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default=None)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    country = CountryField(blank_label='(select country)', null=True)
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

class TeacherProfile(models.Model):
    language = (
        ('english','english'),
        ('french','french'),
        ('spanish','spanish'),
        ('portuguese', 'portuguese'),

    )

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=50, choices=language, default='english')
    website = models.URLField(null=True, blank=True, )
    twitter = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    facebook = models.URLField(null=True)
    youtube = models.URLField(null=True)


    def __str__(self):
        return self.profile.user.username
        