# Generated by Django 5.1.5 on 2025-02-01 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0040_events_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
