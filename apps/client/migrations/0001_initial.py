# Generated by Django 4.2.1 on 2023-06-06 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalClient',
            fields=[
                ('idclient', models.IntegerField(blank=True, db_column='IdClient', db_index=True)),
                ('identificationcard', models.CharField(db_column='IdentificationCard', max_length=10)),
                ('names', models.CharField(db_column='Names', max_length=100)),
                ('lastnames', models.CharField(db_column='Lastname', max_length=100)),
                ('birth_date', models.DateField(db_column='BirthDate')),
                ('photo', models.TextField(blank=True, db_column='Photo', max_length=255, null=True)),
                ('address', models.CharField(db_column='Address', max_length=255)),
                ('email', models.CharField(db_column='Email', max_length=255)),
                ('phone', models.CharField(db_column='Phone', max_length=255)),
                ('cell', models.CharField(db_column='Cell', max_length=255)),
                ('observations', models.CharField(blank=True, db_column='Observations', max_length=255, null=True)),
                ('entry_date', models.DateField(db_column='EntryDate')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('idcellars', models.ForeignKey(blank=True, db_column='IdCellars', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='routes.cellars')),
                ('idcompany', models.ForeignKey(blank=True, db_column='IdCompany', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='company.company')),
            ],
            options={
                'verbose_name': 'historical client',
                'verbose_name_plural': 'historical clients',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('idclient', models.AutoField(db_column='IdClient', primary_key=True, serialize=False)),
                ('identificationcard', models.CharField(db_column='IdentificationCard', max_length=10)),
                ('names', models.CharField(db_column='Names', max_length=100)),
                ('lastnames', models.CharField(db_column='Lastname', max_length=100)),
                ('birth_date', models.DateField(db_column='BirthDate')),
                ('photo', models.ImageField(blank=True, db_column='Photo', max_length=255, null=True, upload_to='photo/')),
                ('address', models.CharField(db_column='Address', max_length=255)),
                ('email', models.CharField(db_column='Email', max_length=255)),
                ('phone', models.CharField(db_column='Phone', max_length=255)),
                ('cell', models.CharField(db_column='Cell', max_length=255)),
                ('observations', models.CharField(blank=True, db_column='Observations', max_length=255, null=True)),
                ('entry_date', models.DateField(db_column='EntryDate')),
                ('idcellars', models.ForeignKey(db_column='IdCellars', on_delete=django.db.models.deletion.CASCADE, to='routes.cellars')),
                ('idcompany', models.ForeignKey(db_column='IdCompany', on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]