# Generated by Django 2.2.6 on 2019-11-04 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20191105_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrrs_intake_screen',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrrs_intake_screen',
            name='Date1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrrs_intake_screen',
            name='Intake_Appointment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrrs_intake_screen',
            name='Rescheduled',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrrs_intake_screen',
            name='date_last_used',
            field=models.DateField(blank=True, null=True),
        ),
    ]
