# Generated by Django 4.2.3 on 2023-07-27 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dersler', '0008_dersler_is_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dersler',
            name='is_liked',
        ),
    ]
