# Generated by Django 5.0.6 on 2024-07-01 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
