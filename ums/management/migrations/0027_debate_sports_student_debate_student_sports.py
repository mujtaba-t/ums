# Generated by Django 4.1.4 on 2023-02-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0026_quiz_quiz_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('participate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('played', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='debate',
            field=models.ManyToManyField(to='management.debate'),
        ),
        migrations.AddField(
            model_name='student',
            name='sports',
            field=models.ManyToManyField(to='management.sports'),
        ),
    ]