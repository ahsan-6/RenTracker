# Generated by Django 4.0.1 on 2022-01-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_duerents_duedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('rent', models.IntegerField()),
                ('propType', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='renter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('property', models.CharField(max_length=200)),
                ('homeAddr', models.CharField(max_length=200)),
                ('phNo', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('amtPaid', models.IntegerField()),
                ('totalRent', models.IntegerField()),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='dueRents',
        ),
    ]
