# Generated by Django 4.2.7 on 2023-11-15 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entries',
            new_name='Events',
        ),
    ]