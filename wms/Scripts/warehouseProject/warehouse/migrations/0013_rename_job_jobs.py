# Generated by Django 4.2.2 on 2023-07-13 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0012_rename_temporary_employee_job_temporary_employe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='Jobs',
        ),
    ]
