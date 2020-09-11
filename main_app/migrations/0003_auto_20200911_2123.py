# Generated by Django 3.0.8 on 2020-09-11 21:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200911_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='quantity',
            new_name='time',
        ),
        migrations.AddField(
            model_name='task',
            name='person',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
