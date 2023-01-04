# Generated by Django 4.1.2 on 2023-01-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CheckGlossary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="Термин")),
                ("description", models.TextField(verbose_name="Описание")),
                ("isFavourite", models.BooleanField(verbose_name="Избранный")),
                ("isChecked", models.BooleanField(verbose_name="Проверено?")),
            ],
            options={
                "verbose_name": "Глоссарий",
                "verbose_name_plural": "Глоссарий",
            },
        ),
        migrations.CreateModel(
            name="Glossary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="Термин")),
                ("description", models.TextField(verbose_name="Описание")),
                ("isFavourite", models.BooleanField(verbose_name="Избранный")),
                ("isChecked", models.BooleanField(verbose_name="Проверено?")),
            ],
        ),
    ]
