# Generated by Django 4.0.1 on 2022-01-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_joined_renter_datejoined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renter',
            name='dateLeft',
            field=models.DateField(blank=True, null=True),
        ),
    ]
