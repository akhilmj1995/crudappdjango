# Generated by Django 5.0 on 2024-01-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='Age',
            field=models.IntegerField(null=True),
        ),
    ]
