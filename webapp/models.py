from django.db import models

# Create your models here.
class picM(models.Model):
    idd=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    pic=models.CharField(max_length=100)

 