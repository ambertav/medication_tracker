# Generated by Django 4.2 on 2023-04-26 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_dose_unit_medication_inactive_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='day_supply',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
