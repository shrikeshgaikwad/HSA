# Generated by Django 5.1.5 on 2025-01-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_students_delete_customstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='mob',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
