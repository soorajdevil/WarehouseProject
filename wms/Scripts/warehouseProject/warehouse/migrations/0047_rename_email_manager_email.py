# Generated by Django 4.2.2 on 2023-07-30 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0046_rename_email_manager_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='Email',
            new_name='email',
        ),
    ]