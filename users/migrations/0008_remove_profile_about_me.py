# Generated by Django 3.2.5 on 2021-08-06 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_teacherprofile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about_me',
        ),
    ]
