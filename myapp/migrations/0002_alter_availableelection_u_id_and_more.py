# Generated by Django 4.2.1 on 2023-10-04 12:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availableelection',
            name='u_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='party_img',
            field=models.ImageField(upload_to='party_img'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='u_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='profile_img',
            field=models.ImageField(upload_to='profile_img'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='u_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='voter_img',
            field=models.ImageField(upload_to='voter_img'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='u_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]