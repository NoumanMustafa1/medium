# Generated by Django 3.2 on 2022-11-16 13:08

import datetime
import django.contrib.auth.models
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20221116_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('api.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Viewer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('api.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 16, 13, 8, 36, 431157, tzinfo=utc)),
        ),
    ]
