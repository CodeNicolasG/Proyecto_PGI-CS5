# Generated by Django 5.1.4 on 2025-01-03 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miembro',
            options={'verbose_name': 'Miembro', 'verbose_name_plural': 'Miembros'},
        ),
        migrations.AlterModelTable(
            name='miembro',
            table='miembros',
        ),
    ]
