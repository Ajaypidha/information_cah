from django.db import models

# Create your models here.
class mycache_table(models.Model):
    name=models.CharField(null=True,blank=True)

