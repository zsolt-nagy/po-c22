# Generated by Django 4.1 on 2022-08-31 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('po_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='end_date',
        ),
    ]
