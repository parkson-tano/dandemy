# Generated by Django 3.2.5 on 2021-08-07 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_competence'),
        ('enroll', '0002_rename_cart_order_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
