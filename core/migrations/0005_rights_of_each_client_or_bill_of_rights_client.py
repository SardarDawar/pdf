# Generated by Django 2.2.6 on 2019-10-27 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191027_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='rights_of_each_client_or_bill_of_rights',
            name='client',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]