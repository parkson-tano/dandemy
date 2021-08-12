# Generated by Django 3.2.5 on 2021-08-05 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_request_requestteacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='RequestTeacher',
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
