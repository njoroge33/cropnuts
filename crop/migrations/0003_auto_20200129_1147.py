# Generated by Django 3.0.2 on 2020-01-29 08:47

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0002_auto_20200129_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crate',
            name='country',
            field=django_countries.fields.CountryField(default='Kenya', max_length=2),
        ),
    ]
