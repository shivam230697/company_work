# Generated by Django 4.2.10 on 2024-02-16 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cns_app', '0012_finalgoods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalgoods',
            name='product_description',
            field=models.CharField(max_length=200),
        ),
    ]
