# Generated by Django 4.2.1 on 2023-06-22 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_historicallocality_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicallocality',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='historicallocality',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='longitude',
        ),
    ]