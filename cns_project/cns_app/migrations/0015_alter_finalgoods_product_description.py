# Generated by Django 4.2.10 on 2024-02-16 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cns_app', '0014_alter_finalgoods_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalgoods',
            name='product_description',
            field=models.CharField(choices=[('option1', '45 mm'), ('option2', '90 mm'), ('option3', 'pencil')], max_length=10),
        ),
    ]
