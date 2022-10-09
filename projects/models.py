import os
from django.db import models
# from personal_portfolio import settings


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='static/img', help_text='image for the project')
    thumbnail = models.FilePathField(path='static/img', help_text='thumbnail for the project')


    def __str__(self):
        return f'{self.id} ({self.title})'