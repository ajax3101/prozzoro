# Generated by Django 4.2.7 on 2023-11-12 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoda', '0007_rename_region_agency_region_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agency',
            old_name='region_id',
            new_name='region',
        ),
    ]
