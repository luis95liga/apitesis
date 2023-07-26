# Generated by Django 4.2.1 on 2023-07-21 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guide', '0012_guidecontent_customsdeclarationnumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUnit',
            fields=[
                ('idunit', models.IntegerField(blank=True, db_column='IdUnit', db_index=True)),
                ('unit', models.CharField(db_column='Unit', max_length=5)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical unit',
                'verbose_name_plural': 'historical units',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('idunit', models.AutoField(db_column='IdUnit', primary_key=True, serialize=False)),
                ('unit', models.CharField(db_column='Unit', max_length=5)),
            ],
        ),
        migrations.RenameField(
            model_name='guidecontentdetailtmp',
            old_name='idguidecontentdetailtpm',
            new_name='idguidecontentdetailtmp',
        ),
        migrations.RenameField(
            model_name='historicalguidecontentdetailtmp',
            old_name='idguidecontentdetailtpm',
            new_name='idguidecontentdetailtmp',
        ),
        migrations.DeleteModel(
            name='HistoricalUnity',
        ),
        migrations.AlterField(
            model_name='guidecontentdetail',
            name='idunit',
            field=models.ForeignKey(db_column='IdUnit', on_delete=django.db.models.deletion.CASCADE, to='guide.unit'),
        ),
        migrations.AlterField(
            model_name='guidecontentdetailtmp',
            name='idunit',
            field=models.ForeignKey(db_column='IdUnit', on_delete=django.db.models.deletion.CASCADE, to='guide.unit'),
        ),
        migrations.AlterField(
            model_name='historicalguidecontentdetail',
            name='idunit',
            field=models.ForeignKey(blank=True, db_column='IdUnit', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='guide.unit'),
        ),
        migrations.AlterField(
            model_name='historicalguidecontentdetailtmp',
            name='idunit',
            field=models.ForeignKey(blank=True, db_column='IdUnit', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='guide.unit'),
        ),
        migrations.DeleteModel(
            name='Unity',
        ),
    ]
