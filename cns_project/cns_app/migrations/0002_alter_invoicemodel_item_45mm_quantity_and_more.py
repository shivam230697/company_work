# Generated by Django 5.0.2 on 2024-02-29 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cns_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicemodel',
            name='item_45mm_quantity',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='item_90mm_quantity',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='item_pencil_quantity',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
