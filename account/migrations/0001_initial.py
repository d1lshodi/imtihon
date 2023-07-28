# Generated by Django 4.2.3 on 2023-07-28 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('address', models.CharField(default='', max_length=65)),
                ('contact', models.CharField(default='', max_length=15)),
                ('picture', models.ImageField(blank=True, upload_to='media/')),
            ],
            options={
                'db_table': 'owner',
            },
        ),
    ]