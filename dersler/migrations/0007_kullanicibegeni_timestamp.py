# Generated by Django 4.2.3 on 2023-07-27 07:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dersler', '0006_yorum'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanicibegeni',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
