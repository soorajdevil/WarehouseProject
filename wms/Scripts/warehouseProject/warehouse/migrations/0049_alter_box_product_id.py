# Generated by Django 4.2.2 on 2023-08-03 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0048_rename_password_manager_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='warehouse.products'),
        ),
    ]
