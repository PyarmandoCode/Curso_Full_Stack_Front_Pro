from .views import index,quienes

from django.urls import path

urlpatterns = [
    path('index/', index),
    path('quienes/', quienes)
]