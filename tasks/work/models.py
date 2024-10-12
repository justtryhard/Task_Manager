from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


class WorkTask(models.Model):           #класс, определяющий атрибуты и архитектуру сущности "Задача"
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
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):              #переопределение метода для показа параметра title при вызове
        return f'{self.title}'

    # def set_closed(self):
    #     self.status = "Закрыта"
    #     return redirect('work_home')

    class Meta:
        verbose_name = "Задачи"
        verbose_name_plural = "Задачи"


class Comments(models.Model):       #класс, определяющий атрибуты комментариев
    worktask = models.ForeignKey(WorkTask, on_delete=models.CASCADE, verbose_name='Задача', blank=True, null=True,
                                 related_name='comments_worktask')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='')
    status = models.BooleanField(verbose_name='Видимость комментария', default=False) #не используется

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'