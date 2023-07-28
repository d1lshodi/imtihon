from rest_framework import serializers
from .models import BronModel,FieldModel




class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldModel
        fields = '__all__'


class BronSeralizer(serializers.ModelSerializer):
    class Meta:
        model = BronModel
        fields = '__all__'
