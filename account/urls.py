from django.urls import path
from  .views import (PersonView,PersonDetailView,OwnerView,OwnerDetailView)

urlpatterns= [
    path('person/',PersonView.as_view()),
    path('person/<pk>/',PersonDetailView.as_view()),
    path('owner/',OwnerView.as_view()),
    path('owner/<pk>/',OwnerDetailView.as_view()),
]