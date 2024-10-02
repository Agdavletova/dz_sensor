from django.urls import path

from .views import SensorAPIList, SensorUpdateAPIView, MeasurementCreateAPIView
from rest_framework import routers




urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorAPIList.as_view()), #получение датчиков и создание
    path('sensors/<int:pk>/', SensorUpdateAPIView.as_view()), #обновление датчика и получение конкретного датчика
    # path('measurements/', MeasurementCreateAPIView.as_view()), #добавление измерения
]
