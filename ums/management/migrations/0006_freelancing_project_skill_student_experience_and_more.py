# Generated by Django 4.1.4 on 2023-01-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_quizquestion_remove_quiz_questions_quiz_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=10)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('discription', models.TextField()),
                ('top_skill', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='experience',
            field=models.ManyToManyField(to='management.experience'),
        ),
        migrations.AddField(
            model_name='student',
            name='freelancing',
            field=models.ManyToManyField(to='management.freelancing'),
        ),
        migrations.AddField(
            model_name='student',
            name='project',
            field=models.ManyToManyField(to='management.project'),
        ),
        migrations.AddField(
            model_name='student',
            name='skill',
            field=models.ManyToManyField(to='management.skill'),
        ),
    ]
