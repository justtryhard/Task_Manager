from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Advert(models.Model):  #класс, определяющий атрибуты и архитектуру сущности "Объявление"

    title = models.CharField(verbose_name='Заголовок', max_length=70)
    content = models.TextField(verbose_name='Содержание')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор', null=True)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):  #переопределение метода для показа параметра title при вызове
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'
