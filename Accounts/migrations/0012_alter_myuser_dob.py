# Generated by Django 4.0.3 on 2022-03-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0011_myuser_address_myuser_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='dob',
            field=models.DateField(),
        ),
    ]
