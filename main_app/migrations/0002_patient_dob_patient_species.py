# Generated by Django 4.2 on 2023-04-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.DateField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='species',
            field=models.CharField(max_length=50),
            preserve_default=False,
        ),
    ]