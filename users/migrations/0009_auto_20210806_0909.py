# Generated by Django 3.2.5 on 2021-08-06 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_profile_about_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
