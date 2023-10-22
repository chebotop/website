# Generated by Django 4.2.4 on 2023-10-22 04:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_shoemodel_created_at_shoemodel_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
