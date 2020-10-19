from django.db import models

# Create your models here.


class Tables(models.Model):
    post = models.CharField(max_length=2000, blank=False, default='')
    x = models.IntegerField(max_length=10, blank=False, default=1)
    y = models.IntegerField(max_length=10, blank=False, default=1)
