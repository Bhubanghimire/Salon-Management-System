# Generated by Django 4.0.3 on 2022-03-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_rename_skills_myuser_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='description',
            field=models.TextField(default=''),
        ),
    ]