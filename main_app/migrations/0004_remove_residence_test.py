# Generated by Django 2.2.6 on 2019-12-24 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20191224_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residence',
            name='test',
        ),
    ]
