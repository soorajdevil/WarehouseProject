# Generated by Django 4.2.2 on 2023-07-13 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0013_rename_job_jobs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
    ]