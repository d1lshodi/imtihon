from pyexpat import model
from django.db import models

from django.db import models
import datetime
from django.contrib.auth.models import User


CHOICE = [
    ('9:00-10:00','9:00-10:00'),
    ('10:00-11:00','10:00-11:00'),
    ('11:00-12:00','11:00-12:00'),
    ('12:00-13:00','12:00-13:00'),
    ('14:00-15:00','14:00-15:00'),
    ('15:00-16:00','15:00-16:00'),
    ('16:00-17:00','16:00-17:00'),
    ('18:00-19:00','18:00-19:00'),
    ('20:00-21:00','20:00-21:00'),
    ('22:00-23:00','22:00-23:00'),
]

class FieldModel(models.Model):
    name = models.CharField(max_length=250, default='')
    address = models.CharField(max_length=250, default='')
    contact = models.CharField(max_length=250, default='')
    price = models.CharField(max_length=250, default='')

    def str(self):
        return self.name

    class Meta:
        db_table = 'field'

class BronModel(models.Model):
    from account.models import UserModel
    user_id = models.ForeignKey(UserModel,on_delete=models.CASCADE, default=None)
    field_id = models.ForeignKey(FieldModel,on_delete=models.CASCADE, default=None)
    bron_date = models.DateField(datetime.datetime.now())
    bron_time = models.CharField(choices=CHOICE)

    def __str__(self) -> str:
        return self.user_id
