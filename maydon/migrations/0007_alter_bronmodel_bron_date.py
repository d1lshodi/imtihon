# Generated by Django 4.2.3 on 2023-07-28 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maydon', '0006_alter_bronmodel_bron_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bronmodel',
            name='bron_date',
            field=models.DateField(verbose_name=datetime.datetime(2023, 7, 28, 9, 35, 14, 927681)),
        ),
    ]
