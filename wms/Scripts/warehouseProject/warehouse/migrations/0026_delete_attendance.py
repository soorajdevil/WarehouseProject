# Generated by Django 4.2.2 on 2023-07-18 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0025_attendance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]