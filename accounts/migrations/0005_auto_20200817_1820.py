# Generated by Django 3.1 on 2020-08-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200817_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(default='default_cover.png', upload_to='cover_images'),
        ),
    ]
