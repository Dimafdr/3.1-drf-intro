from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
