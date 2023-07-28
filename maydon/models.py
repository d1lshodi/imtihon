from django.db import models
import datetime
from django.contrib.auth.models import User


class FieldModel(models.Model):
    name = models.CharField(max_length=250, default='')
    status = models.BooleanField(default=False)
    address = models.CharField(max_length=250, default='')
    contact = models.CharField(max_length=250, default='')
    price = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'field'
