# Generated by Django 4.0.3 on 2022-03-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0018_myuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(),
        ),
    ]