# Generated by Django 4.2.2 on 2023-07-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0040_manager_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervise',
            name='UserType',
            field=models.CharField(default='Supervisor', max_length=100),
        ),
    ]