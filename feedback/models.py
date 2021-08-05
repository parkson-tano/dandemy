from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.CharField(max_length=500, null=True)
    rating = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} reviewed {self.course}'
