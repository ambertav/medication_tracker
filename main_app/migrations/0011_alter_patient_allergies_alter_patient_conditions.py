# Generated by Django 4.2 on 2023-04-29 06:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_patient_allergies_alter_patient_conditions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='patient',
            name='conditions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None),
        ),
    ]
