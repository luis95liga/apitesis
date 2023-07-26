# Generated by Django 4.2.1 on 2023-07-10 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_alter_historicalfixedcosts_options'),
        ('guide', '0007_guide_idvehicle_historicalguide_idvehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='idvehicle',
            field=models.ForeignKey(db_column='IdVehicle', on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle'),
        ),
        migrations.AlterField(
            model_name='historicalguide',
            name='idvehicle',
            field=models.ForeignKey(blank=True, db_column='IdVehicle', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='vehicle.vehicle'),
        ),
    ]