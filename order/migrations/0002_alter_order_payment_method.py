# Generated by Django 5.0.3 on 2024-03-24 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('CBE', 'CBE')], max_length=50),
        ),
    ]