# Generated by Django 5.0.1 on 2024-06-29 18:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"verbose_name": "Статья", "verbose_name_plural": "Статьи"},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
        migrations.AddField(
            model_name="comment",
            name="pub_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата публикации"
            ),
            preserve_default=False,
        ),
    ]
