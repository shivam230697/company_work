# Generated by Django 5.0.2 on 2024-03-11 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cns_app', '0005_rawexpense'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RawExpense',
            new_name='RawExpenseModel',
        ),
    ]
