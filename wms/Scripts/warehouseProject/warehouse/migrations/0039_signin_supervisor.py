# Generated by Django 4.2.2 on 2023-07-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0038_box_building_id_box_product_id_box_rack_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signin_Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]