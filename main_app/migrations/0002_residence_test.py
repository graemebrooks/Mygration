# Generated by Django 2.2.6 on 2019-12-24 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='residence',
            name='test',
            field=models.TextField(default='s'),
            preserve_default=False,
        ),
    ]
