# Generated by Django 3.1.5 on 2021-03-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.FloatField(),
        ),
    ]
