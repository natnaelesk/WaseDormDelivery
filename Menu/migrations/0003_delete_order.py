# Generated by Django 3.2.12 on 2024-03-07 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
