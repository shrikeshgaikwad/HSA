# Generated by Django 5.1.5 on 2025-01-30 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0039_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='year',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
    ]
