# Generated by Django 3.0.3 on 2020-04-19 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='days',
            field=models.CharField(blank=True, choices=[('0', 'MONDAY'), ('1', 'TUESDAY'), ('2', 'WEDNESDAY'), ('3', 'THURSDAY'), ('4', 'FRIDAY'), ('5', 'SATURDAY')], max_length=10),
        ),
        migrations.AddField(
            model_name='timetable',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timetable',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Course',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Date',
            field=models.DateField(),
        ),
    ]
