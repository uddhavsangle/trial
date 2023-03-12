from django.db import models

# Create your models here.
class CurdModel(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    city=models.CharField(max_length=20)
    number=models.BigIntegerField()

