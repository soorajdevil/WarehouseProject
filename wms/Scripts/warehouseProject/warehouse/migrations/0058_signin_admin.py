# Generated by Django 4.2.2 on 2023-09-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0057_chatmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signin_Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
