# Generated by Django 5.0 on 2024-01-15 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_userdb_age_userdb_dob_userdb_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdb',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
