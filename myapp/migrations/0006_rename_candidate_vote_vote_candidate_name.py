# Generated by Django 4.2.1 on 2023-10-07 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_vote_candidate_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='candidate_vote',
            new_name='candidate_name',
        ),
    ]
