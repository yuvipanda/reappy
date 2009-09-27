from django.db import models

ROX_SUX = (('R', 'Rocks'), ('S', 'Sucks'))

# Create your models here.
class Opinion(models.Model):
    user_name = models.CharField(max_length=1024)
    opinion = models.CharField(max_length=1, choices=ROX_SUX)
    text = models.CharField(max_length=140)