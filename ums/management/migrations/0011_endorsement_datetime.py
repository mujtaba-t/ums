# Generated by Django 4.1.4 on 2023-01-21 07:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_endorsement'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsement',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
