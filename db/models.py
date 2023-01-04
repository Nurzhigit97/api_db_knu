
from django.db import models

# Create your models here.


class Glossary(models.Model):
    title = models.CharField(max_length=250, verbose_name="Термин")
    description = models.TextField(verbose_name="Описание")
    isFavourite = models.BooleanField(verbose_name="Избранный")

class CheckAddedGlossaryByUser(models.Model):
    title = models.CharField(max_length=250, verbose_name="Термин")
    description = models.TextField(verbose_name="Описание")
    isChecked = models.BooleanField(verbose_name="Проверено?")
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(max_length=100, verbose_name="Логин")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Глоссарий'
        verbose_name_plural = 'Глоссарий'
