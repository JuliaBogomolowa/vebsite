from django.db import models

class Task(models.Model):
    number = models.IntegerField('Номер')
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    prim = models.CharField('Примечание', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
