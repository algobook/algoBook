from django.db import models

# Create your models here.
class Algo(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=500)
    lang = models.CharField(max_length=10)
    created_at = models.DateTimeField('created_at')
    updated_at = models.DateTimeField('updated_at')
    code = models.CharField(max_length=10000)
    slug = models.CharField(max_length=256)