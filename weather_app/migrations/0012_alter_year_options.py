# Generated by Django 5.0.2 on 2024-03-30 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0011_alter_year_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='year',
            options={'ordering': ['-year'], 'verbose_name_plural': 'Years'},
        ),
    ]