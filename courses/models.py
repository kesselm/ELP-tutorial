from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Course(models.Model):
    title       = models.CharField(max_length=250)
    description = models.TextField()
    author      = models.ForeignKey(User,related_name='courses_created')
    created     = models.DateTimeField(auto_now_add=True)
    publish     = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
