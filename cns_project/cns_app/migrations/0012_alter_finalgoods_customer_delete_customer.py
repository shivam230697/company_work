# Generated by Django 4.2.10 on 2024-02-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cns_app', '0011_alter_customer_customer_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalgoods',
            name='customer',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]