# Generated by Django 4.2.1 on 2023-10-05 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_availableelection_u_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party_img',
            field=models.ImageField(upload_to='party_images'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='profile_img',
            field=models.ImageField(upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='voter_img',
            field=models.ImageField(upload_to='voter_images'),
        ),
    ]