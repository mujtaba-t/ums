# Generated by Django 4.1.4 on 2023-01-21 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
