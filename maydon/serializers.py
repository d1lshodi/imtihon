from rest_framework import serializers
from .models import FieldModel, BronModel


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldModel
        fields = ('name', 'address', 'contact', 'price')


class BronSerializer(serializers.ModelSerializer):
    class Meta:
        model = BronModel
        fields = '__all__'
