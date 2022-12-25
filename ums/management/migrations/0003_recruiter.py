# Generated by Django 4.1.4 on 2022-12-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_publication_publish_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('org_name', models.CharField(max_length=50)),
                ('org_description', models.TextField()),
                ('contact', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
