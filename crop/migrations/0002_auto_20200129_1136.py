# Generated by Django 3.0.2 on 2020-01-29 08:36

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crate',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
