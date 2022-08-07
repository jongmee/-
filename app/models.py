from argparse import _MutuallyExclusiveGroup
import pstats
from django.db import models
from django.conf import settings

class Perfume(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    perfume = models.ForeignKey(Perfume, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.content
