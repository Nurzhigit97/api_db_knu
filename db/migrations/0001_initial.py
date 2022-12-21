# Generated by Django 4.1.2 on 2022-12-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
            ],
            options={
                "verbose_name": "Глоссарий",
                "verbose_name_plural": "Глоссарий",
            },
        ),
    ]