# Generated by Django 3.2.5 on 2021-08-05 23:14

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210805_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherprofile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]
