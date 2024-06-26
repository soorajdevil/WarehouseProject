# Generated by Django 4.2.2 on 2023-07-16 19:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0021_user_employee_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='Time_From',
        ),
        migrations.RemoveField(
            model_name='job',
            name='Time_To',
        ),
        migrations.AddField(
            model_name='job',
            name='ResourceNeeded',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='Time',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
