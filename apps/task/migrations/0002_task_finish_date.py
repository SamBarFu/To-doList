# Generated by Django 2.2.6 on 2020-03-28 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='finish_date',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
    ]