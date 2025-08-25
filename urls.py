from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('stats/', views.car_stats, name='car_stats'),
]
