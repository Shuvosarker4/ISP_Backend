# Generated by Django 5.2.1 on 2025-05-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='payment',
            field=models.CharField(choices=[('cash', 'Cash'), ('card', 'Credit/Debit Card'), ('bank', 'Bank Transfer'), ('online', 'Online Payment')], max_length=100),
        ),
    ]
