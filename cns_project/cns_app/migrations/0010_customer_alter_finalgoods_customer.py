# Generated by Django 4.2.10 on 2024-02-18 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cns_app', '0009_alter_finalgoods_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('customer_address', models.CharField(max_length=100)),
                ('customer_number', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='finalgoods',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cns_app.customer'),
        ),
    ]
