# Generated by Django 4.1.3 on 2022-11-30 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_rename_owner_selection_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selection',
            old_name='users',
            new_name='owner',
        ),
    ]