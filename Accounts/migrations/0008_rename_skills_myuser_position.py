# Generated by Django 4.0.3 on 2022-03-06 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_myuser_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='skills',
            new_name='position',
        ),
    ]