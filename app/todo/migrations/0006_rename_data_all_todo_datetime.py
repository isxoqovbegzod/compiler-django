# Generated by Django 4.0.4 on 2022-04-20 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_rename_data_todo_data_all'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='data_all',
            new_name='datetime',
        ),
    ]
