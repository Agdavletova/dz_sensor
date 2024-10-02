from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название', blank=True)
    description = models.TextField(verbose_name='Описание', blank=False)

    class Meta:
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Температура', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Датчик')
    picture = models.ImageField(blank=False, null=True)

    class Meta:
        verbose_name = "Измерение"
        verbose_name_plural = "Измерения"

    def __str__(self):
        return f"{self.temperature} : {self.sensor}"
