# Generated by Django 3.0.3 on 2020-04-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0002_auto_20200419_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='Venue',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]