# Generated by Django 3.0.8 on 2020-09-11 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
