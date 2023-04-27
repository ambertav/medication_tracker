# Generated by Django 4.2 on 2023-04-26 23:40

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_dose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dose',
            name='unit',
        ),
        migrations.AddField(
            model_name='medication',
            name='inactive_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medication',
            name='quantity',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medication',
            name='refills',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AddField(
            model_name='medication',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='medication',
            name='unit',
            field=models.CharField(default='capsule', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medication',
            name='day_supply',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]