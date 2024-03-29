# Generated by Django 4.2.1 on 2023-06-18 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabulation',
            fields=[
                ('idtabulation', models.AutoField(db_column='IdTabulation', primary_key=True, serialize=False)),
                ('km', models.IntegerField(blank=True, db_column='Km', null=True)),
                ('hours', models.IntegerField(blank=True, db_column='Hours', null=True)),
                ('idcellars', models.ForeignKey(db_column='IdCellars', on_delete=django.db.models.deletion.CASCADE, to='routes.cellars')),
                ('idcompany', models.ForeignKey(db_column='IdCompany', on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('iddestinations', models.ForeignKey(db_column='IdDestinations', on_delete=django.db.models.deletion.CASCADE, to='routes.destinations')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalTabulation',
            fields=[
                ('idtabulation', models.IntegerField(blank=True, db_column='IdTabulation', db_index=True)),
                ('km', models.IntegerField(blank=True, db_column='Km', null=True)),
                ('hours', models.IntegerField(blank=True, db_column='Hours', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('idcellars', models.ForeignKey(blank=True, db_column='IdCellars', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='routes.cellars')),
                ('idcompany', models.ForeignKey(blank=True, db_column='IdCompany', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='company.company')),
                ('iddestinations', models.ForeignKey(blank=True, db_column='IdDestinations', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='routes.destinations')),
            ],
            options={
                'verbose_name': 'historical tabulation',
                'verbose_name_plural': 'historical tabulations',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
