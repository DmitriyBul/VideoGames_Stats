# Generated by Django 3.2 on 2021-05-01 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20210501_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='url',
        ),
    ]
