# Generated by Django 4.2.11 on 2024-03-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weather_app", "0002_alter_year_options_seasonaldata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seasonaldata",
            name="aut",
            field=models.FloatField(max_length=25),
        ),
        migrations.AlterField(
            model_name="seasonaldata",
            name="spr",
            field=models.FloatField(max_length=25),
        ),
        migrations.AlterField(
            model_name="seasonaldata",
            name="sum",
            field=models.FloatField(max_length=25),
        ),
        migrations.AlterField(
            model_name="seasonaldata",
            name="win",
            field=models.FloatField(max_length=25),
        ),
    ]