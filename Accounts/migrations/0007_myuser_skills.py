# Generated by Django 4.0.3 on 2022-03-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_alter_contactus_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='skills',
            field=models.CharField(default=' ', max_length=250),
        ),
    ]