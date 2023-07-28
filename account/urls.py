from django.urls import path
from  .views import OwnerCreateView

urlpatterns= [
    path('createowner/', OwnerCreateView.as_view()),
]