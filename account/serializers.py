from rest_framework import serializers
from .models import PersonModel,OwnerModel,CustomUser

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonModel
        fields=('name','address','contact','picture','user')







class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=OwnerModel
        fields=('field_id')
