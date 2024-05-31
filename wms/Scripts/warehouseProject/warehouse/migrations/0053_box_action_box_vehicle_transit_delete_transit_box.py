# Generated by Django 4.2.2 on 2023-08-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0052_transit_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='Action',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='box',
            name='vehicle_transit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='transit_box',
        ),
    ]
