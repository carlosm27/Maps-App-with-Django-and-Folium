# Generated by Django 3.2.7 on 2021-09-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordenadas',
            name='lat',
            field=models.FloatField(max_length=20),
        ),
        migrations.AlterField(
            model_name='coordenadas',
            name='lon',
            field=models.FloatField(max_length=20),
        ),
    ]