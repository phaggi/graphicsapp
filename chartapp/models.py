from django.db import models


# Create your models here.
class Temperature(models.Model):
    amount = models.DecimalField(max_digits=11, decimal_places=4)
    datetime = models.DateTimeField()
