# Generated by Django 3.2.4 on 2021-06-16 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_taskuser_task_tasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tasks',
            new_name='user',
        ),
    ]
