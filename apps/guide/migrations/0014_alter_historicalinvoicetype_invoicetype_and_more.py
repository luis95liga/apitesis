# Generated by Django 4.2.1 on 2023-07-21 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0013_historicalunit_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalinvoicetype',
            name='invoicetype',
            field=models.CharField(db_column='InvoiceType', max_length=225),
        ),
        migrations.AlterField(
            model_name='historicalunit',
            name='unit',
            field=models.CharField(db_column='Unit', max_length=225),
        ),
        migrations.AlterField(
            model_name='invoicetype',
            name='invoicetype',
            field=models.CharField(db_column='InvoiceType', max_length=225),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit',
            field=models.CharField(db_column='Unit', max_length=225),
        ),
    ]