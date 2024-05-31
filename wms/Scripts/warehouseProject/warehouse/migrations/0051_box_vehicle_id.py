# Generated by Django 4.2.2 on 2023-08-25 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0050_building_total_no_racks'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='vehicle_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='warehouse.veh'),
        ),
    ]