# Generated by Django 5.0 on 2024-01-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0014_userdb_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdb',
            name='dob',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
