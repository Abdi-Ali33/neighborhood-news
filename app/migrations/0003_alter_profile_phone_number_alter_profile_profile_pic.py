# Generated by Django 4.0.5 on 2022-06-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_neighbourhood_area_administrator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile.jfif', upload_to='images/'),
        ),
    ]
