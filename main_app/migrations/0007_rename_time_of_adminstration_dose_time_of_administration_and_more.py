# Generated by Django 4.2 on 2023-04-27 00:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_medication_day_supply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dose',
            old_name='time_of_adminstration',
            new_name='time_of_administration',
        ),
        migrations.AddField(
            model_name='dose',
            name='inactive_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dose',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dose',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
