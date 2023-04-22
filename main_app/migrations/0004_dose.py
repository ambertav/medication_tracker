# Generated by Django 4.2 on 2023-04-22 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_medication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('unit', models.CharField(max_length=50)),
                ('time_of_adminstration', models.TimeField()),
                ('time_interval', models.IntegerField()),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.medication')),
            ],
        ),
    ]
