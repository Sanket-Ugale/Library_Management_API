# Generated by Django 5.0.3 on 2024-03-27 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_blacklistedtoken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlacklistedToken',
        ),
    ]
