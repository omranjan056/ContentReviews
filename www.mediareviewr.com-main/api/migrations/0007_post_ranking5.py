# Generated by Django 3.2 on 2022-06-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220615_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ranking5',
            field=models.IntegerField(default=10000),
        ),
    ]
