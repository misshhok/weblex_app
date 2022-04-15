from tabnanny import verbose
from django.db import models


# Create your models here.

class Table(models.Model):
    title = models.CharField(max_length=127, verbose_name='Название')
    count = models.IntegerField(verbose_name='Колличество')
    distance = models.IntegerField(verbose_name='Расстояние')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Строка(у)'
        verbose_name_plural = 'Строки'
