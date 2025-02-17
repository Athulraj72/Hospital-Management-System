# Generated by Django 5.0 on 2023-12-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_appointmentdb_age_appointmentdb_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('message', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
