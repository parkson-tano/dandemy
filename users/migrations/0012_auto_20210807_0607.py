# Generated by Django 3.2.5 on 2021-08-07 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
