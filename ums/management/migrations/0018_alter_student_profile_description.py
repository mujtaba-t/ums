# Generated by Django 4.1.4 on 2023-01-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0017_teacher_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_description',
            field=models.TextField(),
        ),
    ]