# Generated by Django 5.0.4 on 2024-05-10 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_alter_opiniones_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='opiniones',
            table='tienda_opiniones',
        ),
    ]
