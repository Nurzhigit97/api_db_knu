
from django.db import models

# Create your models here.


class Glossary(models.Model):
    title = models.CharField(max_length=250, verbose_name="Термин")
    description = models.TextField(verbose_name="Описание")
    isFavourite = models.BooleanField(verbose_name="Избранный")
    isChecked = models.BooleanField(verbose_name="Проверено?")

class CheckGlossary(models.Model):
    title = models.CharField(max_length=250, verbose_name="Термин")
    description = models.TextField(verbose_name="Описание")
    isFavourite = models.BooleanField(verbose_name="Избранный")
    isChecked = models.BooleanField(verbose_name="Проверено?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Глоссарий'
        verbose_name_plural = 'Глоссарий'
