# Generated by Django 2.2.5 on 2021-07-19 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0002_auto_20210719_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
    ]
