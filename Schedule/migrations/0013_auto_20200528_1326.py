# Generated by Django 3.0.3 on 2020-05-28 12:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Schedule', '0012_allocatedvenues'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AllocatedVenues',
            new_name='AllocatedVenue',
        ),
    ]
