# Generated by Django 3.1.7 on 2021-03-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('credentials', models.JSONField()),
            ],
        ),
    ]