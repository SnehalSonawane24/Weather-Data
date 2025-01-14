# Generated by Django 4.2.11 on 2024-03-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weather_app", "0004_alter_seasonaldata_win"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seasonaldata",
            name="aut",
            field=models.FloatField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name="seasonaldata",
            name="spr",
            field=models.FloatField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name="seasonaldata",
            name="sum",
            field=models.FloatField(blank=True, max_length=25, null=True),
        ),
    ]
