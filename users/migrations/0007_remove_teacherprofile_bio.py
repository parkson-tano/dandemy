# Generated by Django 3.2.5 on 2021-08-06 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210806_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherprofile',
            name='bio',
        ),
    ]
