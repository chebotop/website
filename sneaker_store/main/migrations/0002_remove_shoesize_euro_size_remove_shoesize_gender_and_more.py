# Generated by Django 4.2.4 on 2023-12-17 16:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoesize',
            name='euro_size',
        ),
        migrations.RemoveField(
            model_name='shoesize',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='shoesize',
            name='sm_size',
        ),
        migrations.AddField(
            model_name='shoesize',
            name='size',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoemodel',
            name='sizes',
            field=models.ManyToManyField(related_name='sizes', to='main.shoesize'),
        ),
        migrations.CreateModel(
            name='ShoeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_images', models.ImageField(upload_to=main.models.shoe_image_directory_path)),
                ('shoe_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.shoemodel')),
            ],
        ),
    ]