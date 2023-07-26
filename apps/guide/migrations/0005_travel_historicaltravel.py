# Generated by Django 4.2.1 on 2023-07-06 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0008_alter_historicalfixedcosts_options'),
        ('guide', '0004_alter_guide_idlocation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('idtravel', models.AutoField(db_column='IdTravel', primary_key=True, serialize=False)),
                ('datestart', models.DateField(db_column='DateStart')),
                ('dateend', models.DateField(db_column='DateEnd')),
                ('dif', models.DecimalField(db_column='Dif', decimal_places=2, max_digits=10)),
                ('feeding', models.DecimalField(db_column='Feeding', decimal_places=2, max_digits=10)),
                ('hours', models.IntegerField(db_column='Hours')),
                ('kml', models.DecimalField(db_column='Kml', decimal_places=2, max_digits=10)),
                ('kmsdes', models.IntegerField(db_column='Kmsdes')),
                ('ltes', models.DecimalField(db_column='Ltes', decimal_places=2, max_digits=10)),
                ('ltgas', models.IntegerField(db_column='Ltgas')),
                ('percentage', models.IntegerField(db_column='Percentage')),
                ('performance', models.DecimalField(db_column='Performance', decimal_places=2, max_digits=10)),
                ('profitability', models.DecimalField(db_column='Profitability', decimal_places=2, max_digits=10)),
                ('salary', models.DecimalField(db_column='Salary', decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(db_column='Subtotal', decimal_places=2, max_digits=10)),
                ('tank', models.DecimalField(db_column='Tank', decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(db_column='Total', decimal_places=2, max_digits=10)),
                ('observations', models.TextField(db_column='Observations')),
                ('guide', models.ManyToManyField(blank=True, db_column='Guide', related_name='guide', to='guide.guide')),
                ('idtrailer', models.ForeignKey(db_column='IdTrailer', on_delete=django.db.models.deletion.CASCADE, to='vehicle.trailer')),
                ('idvehicle', models.ForeignKey(db_column='IdVehicle', on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalTravel',
            fields=[
                ('idtravel', models.IntegerField(blank=True, db_column='IdTravel', db_index=True)),
                ('datestart', models.DateField(db_column='DateStart')),
                ('dateend', models.DateField(db_column='DateEnd')),
                ('dif', models.DecimalField(db_column='Dif', decimal_places=2, max_digits=10)),
                ('feeding', models.DecimalField(db_column='Feeding', decimal_places=2, max_digits=10)),
                ('hours', models.IntegerField(db_column='Hours')),
                ('kml', models.DecimalField(db_column='Kml', decimal_places=2, max_digits=10)),
                ('kmsdes', models.IntegerField(db_column='Kmsdes')),
                ('ltes', models.DecimalField(db_column='Ltes', decimal_places=2, max_digits=10)),
                ('ltgas', models.IntegerField(db_column='Ltgas')),
                ('percentage', models.IntegerField(db_column='Percentage')),
                ('performance', models.DecimalField(db_column='Performance', decimal_places=2, max_digits=10)),
                ('profitability', models.DecimalField(db_column='Profitability', decimal_places=2, max_digits=10)),
                ('salary', models.DecimalField(db_column='Salary', decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(db_column='Subtotal', decimal_places=2, max_digits=10)),
                ('tank', models.DecimalField(db_column='Tank', decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(db_column='Total', decimal_places=2, max_digits=10)),
                ('observations', models.TextField(db_column='Observations')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('idtrailer', models.ForeignKey(blank=True, db_column='IdTrailer', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='vehicle.trailer')),
                ('idvehicle', models.ForeignKey(blank=True, db_column='IdVehicle', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='vehicle.vehicle')),
            ],
            options={
                'verbose_name': 'historical travel',
                'verbose_name_plural': 'historical travels',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]