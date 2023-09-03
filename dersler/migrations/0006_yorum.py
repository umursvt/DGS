# Generated by Django 4.2.3 on 2023-07-24 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dersler', '0005_kullanicibegeni_delete_yorum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icerik', models.TextField()),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('ders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dersler.dersler')),
                ('kullanici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
