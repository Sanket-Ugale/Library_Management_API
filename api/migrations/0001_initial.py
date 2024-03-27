# Generated by Django 5.0.3 on 2024-03-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=100)),
                ('publication_date', models.DateField(null=True)),
                ('isbn', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]