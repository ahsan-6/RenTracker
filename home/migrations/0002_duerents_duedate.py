# Generated by Django 4.0.1 on 2022-01-06 06:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='duerents',
            name='dueDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
