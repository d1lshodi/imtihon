from django.db import models
from django.contrib.auth.models import AbstractUser
from maydon.models import FieldModel


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a', 'Admin'),
        ('o', 'Owner'),
        ('u', 'User'),
    )
    roles = models.CharField(max_length=1, choices=ROLE_CHOICES)


class PersonModel(models.Model):
    name = models.CharField(max_length=65,default='')
    address = models.CharField(max_length=65,default='')
    contact = models.CharField(max_length=15,default='')
    picture = models.ImageField (upload_to='media/',blank=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)
    

    class Meta:
        abstract = True



class OwnerModel(PersonModel):
    field_id = models.ManyToManyField(to=FieldModel)

    class Meta:
        db_table= 'owner'


class UserModel(PersonModel):

    class Meta:
        db_table= 'user'





