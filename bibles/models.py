from django.db import models

# Create your models here.
class Item(models.Model):
    content = models.TextField()
    content_en = models.TextField()
    vers = models.TextField()
    vers_en = models.TextField()
    keyword = models.TextField()