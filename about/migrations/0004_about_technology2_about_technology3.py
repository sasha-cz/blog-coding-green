# Generated by Django 4.2.7 on 2023-11-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_rename_body_2_about_additional_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='technology2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='about',
            name='technology3',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]