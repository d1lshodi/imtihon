from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import OwnerModel
from .serializers import UserRegistrationSerializer , OwnerCreateSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class OwnerCreateView(generics.ListCreateAPIView):
    queryset = OwnerModel.objects.all()
    serializer_class = OwnerCreateSerializer