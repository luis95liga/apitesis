# Generated by Django 4.2.1 on 2023-06-09 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_historicalmaintenamcecosts_acckm_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalmaintenamcecosts',
            name='brakingSystem',
        ),
        migrations.RemoveField(
            model_name='historicalmaintenamcecosts',
            name='electricSystem',
        ),
        migrations.RemoveField(
            model_name='historicalmaintenamcecosts',
            name='engineRepair',
        ),
        migrations.RemoveField(
            model_name='historicalmaintenamcecosts',
            name='ordinaryMaintenance',
        ),
        migrations.RemoveField(
            model_name='historicalmaintenamcecosts',
            name='suspension',
        ),
        migrations.RemoveField(
            model_name='historicalmaintenamcecosts',
            name='tiresAlignment',
        ),
        migrations.RemoveField(
            model_name='historicalmaintenamcecosts',
            name='transmissionSystem',
        ),
        migrations.RemoveField(
            model_name='maintenamcecosts',
            name='brakingSystem',
        ),
        migrations.RemoveField(
            model_name='maintenamcecosts',
            name='electricSystem',
        ),
        migrations.RemoveField(
            model_name='maintenamcecosts',
            name='engineRepair',
        ),
        migrations.RemoveField(
            model_name='maintenamcecosts',
            name='ordinaryMaintenance',
        ),
        migrations.RemoveField(
            model_name='maintenamcecosts',
            name='suspension',
        ),
        migrations.RemoveField(
            model_name='maintenamcecosts',
            name='tiresAlignment',
        ),
        migrations.RemoveField(
            model_name='maintenamcecosts',
            name='transmissionSystem',
        ),
    ]