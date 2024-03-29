# Generated by Django 3.2.5 on 2021-08-02 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_alter_course_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='class_images')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='subject',
        ),
        migrations.AddField(
            model_name='course',
            name='subject_image',
            field=models.ImageField(blank=True, null=True, upload_to='subject_image'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AddField(
            model_name='course',
            name='class_my',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.class'),
        ),
    ]
