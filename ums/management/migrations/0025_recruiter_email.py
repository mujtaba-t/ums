# Generated by Django 4.1.4 on 2023-02-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0024_student_enrollment_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiter',
            name='email',
            field=models.CharField(default='test@test.com', max_length=150),
            preserve_default=False,
        ),
    ]
