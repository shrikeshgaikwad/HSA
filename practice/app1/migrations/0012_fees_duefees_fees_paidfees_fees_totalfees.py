# Generated by Django 5.1.5 on 2025-01-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_students_std'),
    ]

    operations = [
        migrations.AddField(
            model_name='fees',
            name='dueFees',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fees',
            name='paidFees',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fees',
            name='totalFees',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
