# Generated by Django 3.1.5 on 2021-03-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210311_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
