# Generated by Django 5.0.1 on 2024-02-28 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_bio_remove_profile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
