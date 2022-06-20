# Generated by Django 4.0.5 on 2022-06-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='area_administrator',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='health_tell',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='police_number',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='Health_Contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='Police_Contact',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
