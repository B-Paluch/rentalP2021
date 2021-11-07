from django.db import models


# Create your models here.

class RentItem(models.Model):
    id = models.IntegerField(primary_key = True)
    rentItemName = models.CharField(max_length=50, null=False)
    rentState = models.BooleanField(default=None, blank=True, null=True)
    name = models.CharField(max_length=50, default=None, blank=True, null=True)
    surname = models.CharField(max_length=50, default=None, blank=True, null=True)
    rentDate = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name
