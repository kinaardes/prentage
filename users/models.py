from django.db import models

# Create your models here.


class profile(models.Model):
    # name= models.CharField(max_length=100)
    # user_name = models.Char
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
