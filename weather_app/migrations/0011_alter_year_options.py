# Generated by Django 5.0.2 on 2024-03-30 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0010_alter_finaltotal_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='year',
            options={'ordering': ['id', '-year'], 'verbose_name_plural': 'Years'},
        ),
    ]
