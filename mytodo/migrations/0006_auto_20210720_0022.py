# Generated by Django 2.2.5 on 2021-07-19 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0005_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tasks',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='comlete',
            new_name='complete',
        ),
    ]