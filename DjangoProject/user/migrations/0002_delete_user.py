# Generated by Django 4.2 on 2023-04-19 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_delete_purchase'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
