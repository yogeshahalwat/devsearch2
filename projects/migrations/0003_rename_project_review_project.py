# Generated by Django 4.1.2 on 2022-12-30 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='project',
            new_name='Project',
        ),
    ]
