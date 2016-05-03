from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User, Group

class Course(models.Model):
    title       = models.CharField(max_length=250)
    description = models.TextField()
    author      = models.ForeignKey(User,related_name='courses_created')
    # group       = forms.ModelChoiceField(queryset=Group.objects.all(),
    #                                required=True)
    group       = models.ForeignKey(Group,related_name='courses_group',default='Gruppe1')
    created     = models.DateTimeField(auto_now_add=True)
    publish     = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
