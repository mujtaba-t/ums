# Generated by Django 4.1.4 on 2023-01-22 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_certification'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
