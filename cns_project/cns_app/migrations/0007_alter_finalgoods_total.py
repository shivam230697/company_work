# Generated by Django 4.2.10 on 2024-02-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cns_app', '0006_alter_finalgoods_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalgoods',
            name='total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=12, null=True),
        ),
    ]