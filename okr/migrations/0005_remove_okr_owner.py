# Generated by Django 2.1.5 on 2022-02-28 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('okr', '0004_auto_20220225_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='okr',
            name='owner',
        ),
    ]
