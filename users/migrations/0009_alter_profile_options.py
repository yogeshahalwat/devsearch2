# Generated by Django 4.1.2 on 2023-03-20 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]