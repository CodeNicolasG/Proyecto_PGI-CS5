# Generated by Django 5.1.4 on 2025-03-25 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_miembro_options_alter_miembro_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2025, 3, 25, 17, 7, 7, 984880, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
