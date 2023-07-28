from config import permissions
from rest_framework import generics
from .models import FieldModel,BronModel
from .serializers import FieldSerializer,BronSeralizer
from .permissions import FieldPermission


class FieldView(generics.ListAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldSerializer


class BronView(generics.ListCreateView):
    queryset = FieldModel.objects.all()
    serializer_class = BronModel

class BronDeleteView(generics.RetriveDestroyUpdateAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = BronModel
    permissions = FieldPermission
