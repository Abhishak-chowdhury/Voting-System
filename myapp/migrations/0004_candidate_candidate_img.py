# Generated by Django 4.2.1 on 2023-10-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_candidate_party_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='candidate_img',
            field=models.ImageField(null=True, upload_to='candi_images'),
        ),
    ]
