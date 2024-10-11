from django.db import models
from django.conf import settings


class WorkTask(models.Model):
    type_choices = [
        ("Подключение", "Подключение"),
        ("Аварийный выезд", "Аварийный выезд"),
        ("Модернизация", "Модернизация"),
        ("Демонтаж", "Демонтаж")
    ]

    status_choices = [
        ("Открыта", "Открыта"),
        ("Закрыта", "Закрыта")
    ]

    title = models.CharField('Адрес', max_length=50)
    type = models.CharField(max_length=15, choices=type_choices, default="Аварийный выезд")
    description = models.TextField('Описание')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                               verbose_name="Постановщик", related_name="author")
    executor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                 verbose_name="Исполнитель", related_name="executor")
    status = models.CharField(max_length=7, choices=status_choices, default="Открыта")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Tasks for the installers"
        verbose_name_plural = "Tasks for the installers"