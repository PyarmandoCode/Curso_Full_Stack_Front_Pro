from django.urls import path
from .views import index,driver_car

urlpatterns = [
    path('',index,name="index"),
    path('<int:pk>/',driver_car,name="driver"),
]
