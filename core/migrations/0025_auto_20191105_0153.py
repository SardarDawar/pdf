# Generated by Django 2.2.6 on 2019-11-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20191105_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrrs_progress_note',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrrs_record_release_authorization',
            name='Date_of_Birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='initial_treatment_plan',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='initial_treatment_plan',
            name='Discharge_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='initial_treatment_plan',
            name='Review_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
