# Generated by Django 2.2.5 on 2021-07-19 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0003_remove_task_created'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Tasks',
        ),
    ]
