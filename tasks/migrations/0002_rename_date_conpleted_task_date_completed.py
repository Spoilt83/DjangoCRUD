# Generated by Django 5.0.3 on 2024-03-30 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date_conpleted',
            new_name='date_completed',
        ),
    ]
