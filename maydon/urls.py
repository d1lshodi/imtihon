from django.urls import path
from .views import RetrieveView

urlpatterns = [
    path('<pk>', RetrieveView.as_view()),
]
