# Generated by Django 4.1.3 on 2022-11-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(max_length=2000, null=True, verbose_name='Описание'),
        ),
    ]
