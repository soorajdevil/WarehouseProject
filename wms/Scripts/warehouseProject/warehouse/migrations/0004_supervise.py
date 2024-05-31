# Generated by Django 4.2.2 on 2023-07-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_alter_user_employee_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('DOB', models.DateField(null=True)),
                ('gender', models.CharField(max_length=100)),
                ('contact_no', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]