from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import BronModel, FieldModel
from .permissions import IsOwnerPermission
from .serializers import FieldSerializer, BronSerializer


# Create your views here.
class AllCrateFieldView(generics.ListAPIView):
    pass


class RetrieveView(generics.RetrieveAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldSerializer
    permission_classes = (IsOwnerPermission,)
