# Generated by Django 4.2.7 on 2023-11-17 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_entries_events'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]
