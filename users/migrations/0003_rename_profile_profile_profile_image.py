# Generated by Django 4.1.2 on 2023-01-12 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='profile_image',
        ),
    ]
