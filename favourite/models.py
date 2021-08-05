from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
# Create your models here.


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course, null=True, blank=True, related_name='user_favorite')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} favorite'