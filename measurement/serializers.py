from rest_framework import serializers

from .models import Measurement, Sensor


# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):
    measurements = serializers.SlugRelatedField(read_only=True, many=True, slug_field='temperature')
    class Meta:
        model = Sensor
        fields =['id', 'name', 'description', 'measurements']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor', 'picture']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer( read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

