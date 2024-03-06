# Generated by Django 4.2.1 on 2023-08-25 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("assets", "0004_alter_assetslog_asset"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetslog",
            name="employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employeelog",
                to="assets.employeemodel",
            ),
        ),
    ]
