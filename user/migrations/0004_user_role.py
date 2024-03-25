# Generated by Django 3.2.12 on 2024-03-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('restaurant_owner', 'Restaurant Owner'), ('delivery_person', 'Delivery Person'), ('admin', 'Admin')], default='customer', max_length=20),
        ),
    ]