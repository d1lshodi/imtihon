from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import PersonModel,OwnerModel
from .serializers import (PersonSerializer,OwnerSerializer)
from .permissions import IsOwnerPermission


class PersonView(generics.CreateAPIView):
    queryset=PersonModel.objects.all()
    serializer_class=PersonSerializer
    permission_classes=(IsOwnerPermission,)

class PersonDetailView(generics.RetrieveAPIView):
    queryset=PersonModel.objects.all()
    serializer_class=PersonSerializer
    permission_classes=(IsOwnerPermission,)

class PersonCreateView(generics.ListCreateAPIView):
    queryset=PersonModel.object.all()
    serializer_class=PersonSerializer


class PersonDeleteView(generics.ListCreateAPIView):
    queryset=PersonModel.object.all()
    serializer_class=PersonSerializer


class OwnerView(generics.ListCreateAPIView):
    queryset=OwnerModel.object.all()
    serializer_class=OwnerSerializer
    permission_classes=(IsOwnerPermission,)

class OwnerDetailView(generics.RetrieveAPIView):
    queryset=OwnerModel.object.all()
    serializer_class=OwnerSerializer
    permission_classes=(IsOwnerPermission,)

class OwnerDeleteView(generics.ListAPIView):
    queryset=OwnerModel.object.all()
    serializer_class=OwnerSerializer


