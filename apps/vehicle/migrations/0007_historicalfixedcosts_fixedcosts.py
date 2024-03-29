# Generated by Django 4.2.1 on 2023-06-10 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0006_alter_historicalmaintenamcecosts_total_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historicalfixedcosts',
            fields=[
                ('idfixedcosts', models.IntegerField(blank=True, db_column='IdFixedCosts', db_index=True)),
                ('andeanPolicy', models.DecimalField(db_column='AndeanPolicy', decimal_places=2, max_digits=10)),
                ('financialCosts', models.DecimalField(db_column='FinancialCosts', decimal_places=2, max_digits=10)),
                ('insurance', models.DecimalField(db_column='Insurance', decimal_places=2, max_digits=10)),
                ('satelliteTracking', models.DecimalField(db_column='SatelliteTracking', decimal_places=2, max_digits=10)),
                ('technicalReviews', models.DecimalField(db_column='TechnicalReviews', decimal_places=2, max_digits=10)),
                ('vehicleRegistration', models.DecimalField(db_column='VehicleRegistration', decimal_places=2, max_digits=10)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('idvehicle', models.ForeignKey(blank=True, db_column='IdtVehicle', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='vehicle.vehicle')),
            ],
            options={
                'verbose_name': 'historical fixedcosts',
                'verbose_name_plural': 'historical fixedcostss',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='fixedcosts',
            fields=[
                ('idfixedcosts', models.AutoField(db_column='IdFixedCosts', primary_key=True, serialize=False)),
                ('andeanPolicy', models.DecimalField(db_column='AndeanPolicy', decimal_places=2, max_digits=10)),
                ('financialCosts', models.DecimalField(db_column='FinancialCosts', decimal_places=2, max_digits=10)),
                ('insurance', models.DecimalField(db_column='Insurance', decimal_places=2, max_digits=10)),
                ('satelliteTracking', models.DecimalField(db_column='SatelliteTracking', decimal_places=2, max_digits=10)),
                ('technicalReviews', models.DecimalField(db_column='TechnicalReviews', decimal_places=2, max_digits=10)),
                ('vehicleRegistration', models.DecimalField(db_column='VehicleRegistration', decimal_places=2, max_digits=10)),
                ('idvehicle', models.ForeignKey(db_column='IdtVehicle', on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle')),
            ],
        ),
    ]
