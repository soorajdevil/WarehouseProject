# Generated by Django 4.2.2 on 2023-09-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0059_racks_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervise',
            name='id',
        ),
        migrations.AlterField(
            model_name='supervise',
            name='supervisor_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
