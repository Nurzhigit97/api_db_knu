
from django.db import models

# Create your models here.


class Glossary(models.Model):
    title = models.CharField(max_length=250, verbose_name="Термин")
    description = models.TextField(verbose_name="Описание")

class FavouriteGlossary(models.Model):
    title = models.CharField(max_length=100, verbose_name="Термин")
    description = models.CharField(max_length=200, verbose_name="Описание")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Глоссарий'
        verbose_name_plural = 'Глоссарий'
