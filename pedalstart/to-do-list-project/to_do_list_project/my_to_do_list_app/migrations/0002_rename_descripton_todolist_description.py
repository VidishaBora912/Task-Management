# Generated by Django 5.0.4 on 2024-04-05 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_list_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='descripton',
            new_name='description',
        ),
    ]
