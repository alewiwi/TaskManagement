# Generated by Django 3.2.4 on 2021-06-16 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_task_taskuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='TaskUser',
            new_name='tasks',
        ),
    ]
