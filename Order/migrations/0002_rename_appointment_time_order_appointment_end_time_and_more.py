# Generated by Django 4.0.3 on 2022-03-12 07:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='appointment_time',
            new_name='appointment_end_time',
        ),
        migrations.AddField(
            model_name='order',
            name='appointment_start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
