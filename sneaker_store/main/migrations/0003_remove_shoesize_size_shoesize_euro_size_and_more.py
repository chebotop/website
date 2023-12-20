# Generated by Django 4.2.4 on 2023-12-17 16:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_shoesize_euro_size_remove_shoesize_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoesize',
            name='size',
        ),
        migrations.AddField(
            model_name='shoesize',
            name='euro_size',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoesize',
            name='gender',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoesize',
            name='sm_size',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]