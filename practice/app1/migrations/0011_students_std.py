# Generated by Django 5.1.5 on 2025-01-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_remove_students_std'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='std',
            field=models.IntegerField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
