# Generated by Django 4.1.4 on 2023-01-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='designation',
            field=models.TextField(default='Lecturer'),
            preserve_default=False,
        ),
    ]