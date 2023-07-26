# Generated by Django 4.2.1 on 2023-06-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicallocality',
            name='latitude',
            field=models.FloatField(blank=True, db_column='Latitude', null=True),
        ),
        migrations.AddField(
            model_name='historicallocality',
            name='longitude',
            field=models.FloatField(blank=True, db_column='Longitude', null=True),
        ),
        migrations.AddField(
            model_name='locality',
            name='latitude',
            field=models.FloatField(blank=True, db_column='Latitude', null=True),
        ),
        migrations.AddField(
            model_name='locality',
            name='longitude',
            field=models.FloatField(blank=True, db_column='Longitude', null=True),
        ),
    ]
