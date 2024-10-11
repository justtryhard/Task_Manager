from django.db import models


class WorkTask(models.Model):
    title = models.CharField('Адрес', max_length=50)
    type = models.CharField('Тип задачи', max_length=50)
    description = models.TextField('Описание')
    closed = models.BooleanField(default=1)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Tasks for the installers"
        verbose_name_plural = "Tasks for the installers"