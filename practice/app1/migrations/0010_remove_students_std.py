# Generated by Django 5.1.5 on 2025-01-19 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_fees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='std',
        ),
    ]
