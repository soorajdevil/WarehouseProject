# Generated by Django 4.2.2 on 2023-09-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0055_attendenceform_current_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendenceform',
            name='current_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]