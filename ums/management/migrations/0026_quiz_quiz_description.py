# Generated by Django 4.1.4 on 2023-02-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0025_recruiter_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_description',
            field=models.TextField(default='This is a test description for the Quiz'),
            preserve_default=False,
        ),
    ]
