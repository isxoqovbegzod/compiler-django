# Generated by Django 4.0.4 on 2022-04-20 04:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
