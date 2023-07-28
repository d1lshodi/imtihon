from django.urls import path
from  .views import FieldView,BronView,BronDeleteView

urlpatterns= [
    path('maydon/',FieldView.as_view()),
    path('bron/',BronView.as_view()),
    path('maydon/<pk>',BronDeleteView.as_view()),
]