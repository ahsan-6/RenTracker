# Generated by Django 4.0.1 on 2022-01-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_properties_user_renter_user_alter_transaction_renter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renter',
            name='phNo',
            field=models.CharField(max_length=10),
        ),
    ]
