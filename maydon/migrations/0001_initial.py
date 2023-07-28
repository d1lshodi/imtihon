# Generated by Django 4.2.3 on 2023-07-28 04:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('status', models.BooleanField(default=False)),
                ('address', models.CharField(default='', max_length=250)),
                ('contact', models.CharField(default='', max_length=250)),
                ('price', models.CharField(default='', max_length=250)),
                ('bron_date', models.DateField(default=datetime.datetime(2023, 7, 28, 4, 47, 46, 97440))),
            ],
            options={
                'db_table': 'field',
            },
        ),
    ]
